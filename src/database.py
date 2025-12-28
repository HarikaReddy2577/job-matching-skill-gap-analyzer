import sqlite3

conn = sqlite3.connect("database/job_matching.db")
cursor = conn.cursor()

# -----------------------------
# MAP USER SKILLS
# -----------------------------

# (user_id, skill_id, proficiency)
user_skills = [
    (1, 1, 3),  # Harika -> Python
    (1, 2, 2),  # Harika -> SQL
    (2, 1, 4),  # Amit -> Python
    (2, 3, 3),  # Amit -> ML
    (3, 4, 2)   # Sara -> Data Analysis
]

cursor.executemany(
    "INSERT INTO user_skills (user_id, skill_id, proficiency) VALUES (?, ?, ?)",
    user_skills
)

# -----------------------------
# MAP JOB SKILLS
# -----------------------------

# (job_id, skill_id, importance)
job_skills = [
    (1, 2, 3),  # Data Analyst -> SQL
    (1, 4, 4),  # Data Analyst -> Data Analysis
    (2, 1, 4),  # ML Engineer -> Python
    (2, 3, 5),  # ML Engineer -> ML
    (3, 1, 3),  # Backend -> Python
    (3, 5, 2)   # Backend -> Docker
]

cursor.executemany(
    "INSERT INTO job_skills (job_id, skill_id, importance) VALUES (?, ?, ?)",
    job_skills
)

conn.commit()
conn.close()

print("✅ User skills and job skills mapped successfully!")
