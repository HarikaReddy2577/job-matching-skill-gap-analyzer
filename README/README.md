# Job Matching & Skill Gap Analyzer

## 📌 Project Overview
This project is an end-to-end Job Matching and Skill Gap Analysis system built using **Python and SQL**.  
It matches candidates to jobs based on skill overlap and experience, ranks jobs by match score, and explains **which skills are missing** for each job.

This system simulates how real-world job portals and ATS (Applicant Tracking Systems) work.

---

## 🎯 Key Features
- Relational database design using SQLite
- Skill-based job matching with weighted scoring
- Job ranking from best to worst match
- Skill gap analysis (explainable recommendations)
- Python–SQL integration
- Beginner-friendly but industry-relevant architecture

---

## 🧠 How It Works
1. Users and jobs are stored in a SQL database
2. Skills are mapped to users (with proficiency)
3. Skills are mapped to jobs (with importance)
4. Matching score is calculated using weighted overlap
5. Missing skills are identified using SQL queries
6. Jobs are ranked and displayed with explanations

---

## 🗄️ Database Schema
Tables used:
- users
- jobs
- skills
- user_skills
- job_skills

---

## 🛠️ Tech Stack
- Python
- SQLite
- SQL
- VS Code
- Jupyter Notebook

---

## 📊 Sample Output

Job: Machine Learning Engineer  
Match Score: 50%  
Missing Skills:
- Machine Learning  

---

## 🚀 Future Improvements
- Use cosine similarity / TF-IDF for ML-based matching
- Resume parsing using NLP
- Web UI using Streamlit
- User authentication
- Real job scraping

---

## 👩‍💻 Author
Harika
