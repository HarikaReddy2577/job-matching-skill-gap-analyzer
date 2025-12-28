# Job Matching & Skill Gap Analyzer

## Project Overview
The Job Matching & Skill Gap Analyzer is an end-to-end application built using Python, SQL, and Streamlit.  
It recommends suitable jobs for users based on their skills and experience, ranks jobs using a weighted matching algorithm, and clearly explains which skills are missing for each job.

This project simulates how real-world job portals and applicant tracking systems (ATS) perform candidate–job matching.


## Key Features
- Relational database design using SQLite
- Skill-based job matching with weighted scoring
- Job ranking from best to worst match
- Skill gap analysis with explainable results
- Python and SQL integration
- Interactive Streamlit web interface

## System Architecture
1. User, job, and skill data are stored in a relational database
2. Skills are mapped to users with proficiency levels
3. Skills are mapped to jobs with importance weights
4. A matching score is calculated based on skill overlap
5. Missing skills are identified using SQL queries
6. Results are displayed through a Streamlit UI

## Database Schema
The project uses the following tables:
- users
- jobs
- skills
- user_skills
- job_skills

These tables form many-to-many relationships between users, jobs, and skills.


## Tech Stack
- Python
- SQLite
- SQL
- Streamlit
- VS Code


## Application Screenshots

### Home Screen
![Home Screen](screenshots/ui_home.png)

### Job Match Results
![Job Results](screenshots/ui_results.png)

## Sample Output
For a selected user, the system displays:
- Job title
- Match score (percentage)
- Missing skills required for the job

Example:
- Job: Backend Developer  
  Match Score: 60%  
  Missing Skills: Docker  


## How to Run the Project Locally

1. Clone the repository:
   git clone https://github.com/your-username/job-matching-skill-gap-analyzer.git

2. Navigate to the project folder:
   cd job-matching-skill-gap-analyzer

3. Install dependencies:
   pip install streamlit

4. Run the application:
   streamlit run app.py

5. Open the browser at:
   http://localhost:8501

Future Enhancements

Machine learning–based similarity using TF-IDF and cosine similarity
Future Enhancements

Machine learning–based similarity using TF-IDF and cosine similarity
Resume parsing using NLP
Real-time job data scraping
User authentication
Deployment on Streamlit Cloud





   
