import sqlite3

# connect to database
conn = sqlite3.connect("database/job_matching.db")
cursor = conn.cursor()

def get_missing_skills(user_id, job_id):
    """
    Returns a list of missing skill names
    """

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
    missing = cursor.fetchall()

    return [skill[0] for skill in missing]

# -----------------------------
# TEST CASE
# User 1 (Harika) & Job 2 (ML Engineer)
# -----------------------------

user_id = 2   # Harika
job_id = 2    # Machine Learning Engineer

missing_skills = get_missing_skills(user_id, job_id)

print(f"Missing skills for user {user_id} for job {job_id}:\n")

if missing_skills:
    for skill in missing_skills:
        print("-", skill)
else:
    print("No missing skills! Perfect match 🎉")

conn.close()
