import sqlite3

# connect to database
conn = sqlite3.connect("database/job_matching.db")
cursor = conn.cursor()

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

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

    if max_score == 0:
        return 0

    return round((score / max_score) * 100, 2)

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

# -----------------------------
# MAIN REPORT FUNCTION
# -----------------------------

def job_match_report(user_id):
    cursor.execute("SELECT job_id, title FROM jobs")
    jobs = cursor.fetchall()

    user_skills = get_user_skills(user_id)
    report = []

    for job_id, title in jobs:
        job_skills = get_job_skills(job_id)
        score = calculate_match_score(user_skills, job_skills)
        missing = get_missing_skills(user_id, job_id)

        report.append({
            "job": title,
            "score": score,
            "missing_skills": missing
        })

    report.sort(key=lambda x: x["score"], reverse=True)
    return report

# -----------------------------
# TEST FOR USER 1 (Harika)
# -----------------------------

user_id = 1
results = job_match_report(user_id)

print("\nJOB MATCH REPORT\n")

for r in results:
    print(f"Job: {r['job']}")
    print(f"Match Score: {r['score']}%")

    if r["missing_skills"]:
        print("Missing Skills:")
        for skill in r["missing_skills"]:
            print(f" - {skill}")
    else:
        print("Missing Skills: None 🎉")

    print("-" * 30)

conn.close()
