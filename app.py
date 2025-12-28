import streamlit as st
import sqlite3

# connect to database
conn = sqlite3.connect("database/job_matching.db")
cursor = conn.cursor()

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def get_users():
    cursor.execute("SELECT user_id, name FROM users")
    return cursor.fetchall()

def get_user_skills(user_id):
    cursor.execute(
        "SELECT skill_id, proficiency FROM user_skills WHERE user_id = ?",
        (user_id,)
    )
    return dict(cursor.fetchall())

def get_job_skills(job_id):
    cursor.execute(
        "SELECT skill_id, importance FROM job_skills WHERE job_id = ?",
        (job_id,)
    )
    return dict(cursor.fetchall())

def calculate_match_score(user_skills, job_skills):
    score = 0
    max_score = 0
    for skill_id, importance in job_skills.items():
        max_score += importance
        if skill_id in user_skills:
            score += min(user_skills[skill_id], importance)
    return round((score / max_score) * 100, 2) if max_score else 0

def get_missing_skills(user_id, job_id):
    query = """
    SELECT s.skill_name
    FROM job_skills js
    JOIN skills s ON js.skill_id = s.skill_id
    WHERE js.job_id = ?
    AND js.skill_id NOT IN (
        SELECT skill_id FROM user_skills WHERE user_id = ?
    )
    """
    cursor.execute(query, (job_id, user_id))
    return [row[0] for row in cursor.fetchall()]

def job_match_report(user_id):
    cursor.execute("SELECT job_id, title FROM jobs")
    jobs = cursor.fetchall()
    user_skills = get_user_skills(user_id)

    report = []
    for job_id, title in jobs:
        job_skills = get_job_skills(job_id)
        score = calculate_match_score(user_skills, job_skills)
        missing = get_missing_skills(user_id, job_id)
        report.append((title, score, missing))

    report.sort(key=lambda x: x[1], reverse=True)
    return report

# -----------------------------
# STREAMLIT UI
# -----------------------------

st.title("Job Matching & Skill Gap Analyzer")

users = get_users()
user_dict = {name: uid for uid, name in users}

selected_user = st.selectbox("Select User", user_dict.keys())

if st.button("Find Job Matches"):
    results = job_match_report(user_dict[selected_user])

    for job, score, missing in results:
        st.subheader(job)
        st.write(f"Match Score: **{score}%**")

        if missing:
            st.write("Missing Skills:")
            for skill in missing:
                st.write(f"- {skill}")
        else:
            st.write("Perfect Match 🎉")

        st.divider()

conn.close()

