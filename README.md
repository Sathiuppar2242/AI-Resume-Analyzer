# ResumeAI - AI Resume Analyzer

ResumeAI is an AI-powered web application that analyzes a candidate's resume based on a specific job description.

The application checks the resume for relevant skills, calculates a resume score, identifies missing skills, and provides suggestions to improve the resume for the selected job role.

## Project Overview

Finding out whether a resume is suitable for a particular job can take a lot of time.

ResumeAI makes this process easier by allowing users to upload their resume and enter the complete job description. The application then analyzes both and provides a clear report showing how well the resume matches the job requirements.

The project is designed as a simple and user-friendly web application that can be used by students, job seekers, and developers.

## Features

- Upload resume in PDF or DOCX format
- Validate uploaded resume files
- Enter complete job descriptions
- Automatically detect the relevant job role
- Identify required skills from the job description
- Find skills available in the resume
- Identify missing skills
- Calculate skill match percentage
- Calculate overall resume score
- Display resume strengths
- Display resume weaknesses
- Provide resume improvement recommendations
- Show animated skill match progress bar
- Display analysis loading screen
- Display clear error messages
- Generate downloadable PDF analysis report
- Responsive web interface
- Simple and easy-to-use design

## Technologies Used

### Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates

### Backend

- Python
- Flask

### Resume Processing

- PDF resume parsing
- DOCX resume parsing
- Regular expression based skill matching

### Other Tools

- Git
- GitHub
- VS Code
- Python Virtual Environment

## How the Project Works

The application follows a simple process.

1. The user opens the ResumeAI website.
2. The user uploads a resume.
3. The application validates the uploaded file.
4. The user enters the complete job description.
5. The application extracts text from the resume.
6. The application analyzes the job description.
7. The application detects the most relevant job role.
8. Required skills are identified.
9. Resume skills are compared with the required skills.
10. The skill match percentage is calculated.
11. Missing skills are identified.
12. An overall resume score is calculated.
13. Strengths, weaknesses, and recommendations are generated.
14. The final analysis is displayed on the results page.
15. The user can download the analysis as a PDF report.

## Resume Score

The application calculates the overall resume score using multiple factors.

The score considers:

- Skill match
- Projects
- Education
- Experience or internship information

The final score is limited to a maximum of 100%.

## Skill Matching

ResumeAI compares the skills required for a particular job with the skills found in the uploaded resume.

For example, if a Python Developer job requires:

- Python
- Flask
- Django
- SQL
- Git
- REST API

and the resume contains:

- Python
- Flask
- SQL
- Git

the application identifies:

### Matched Skills

- Python
- Flask
- SQL
- Git

### Missing Skills

- Django
- REST API

The application then calculates the skill match percentage based on the required skills.

## Supported Job Roles

The current version includes skill matching for several common roles:

- Python Developer
- Java Developer
- Web Developer
- Data Scientist
- Machine Learning Engineer
- Data Analyst
- Frontend Developer
- Backend Developer
- Full Stack Developer
- SQL Developer

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
│
├── services/
│   ├── resume_parser.py
│   └── ai_analyzer.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── uploads/
│
├── ├── .gitignore
├── requirements.txt
└── README.md

The uploads folder is used locally to temporarily store uploaded resumes.

Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project folder
cd AI-Resume-Analyzer
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

On Windows:

venv\Scripts\activate
5. Install the required packages
pip install -r requirements.txt
Running the Application

After activating the virtual environment, run:

python app.py

The application will start on:

http://127.0.0.1:5000/

Open this address in your browser.

Using the Application
Step 1

Upload your resume.

Supported formats:

PDF
DOCX
Step 2

Enter the complete job description.

For example:

We are looking for a Python Developer with experience in Python,
Flask, Django, SQL, Git and REST API development.
Step 3

Click the analyze button.

Step 4

Wait for the resume analysis to complete.

Step 5

View the results.

The results page displays:

Overall Resume Score
Skill Match Percentage
Matched Skills
Missing Skills
Required Skills
Strengths
Weaknesses
Recommendations
Step 6

Download the analysis report as a PDF.

Error Handling

The application validates common user errors such as:

Resume not uploaded
Empty resume filename
Unsupported file type
Empty job description
Resume processing errors
Analysis errors

Clear error messages are displayed to help the user understand the problem.

PDF Report

ResumeAI also provides a downloadable PDF report.

The report contains important analysis information such as:

Resume name
Overall score
Skill match percentage
Matched skills
Missing skills
Strengths
Weaknesses
Recommendations

This allows users to save the analysis for future reference.

GitHub Development

The project was developed incrementally using Git.

Different features were implemented and committed separately, including:

Project foundation
ResumeAI homepage
Visual assets
Skill match progress bar
Resume analysis results
Job description input
Resume upload validation
Loading screen
Error handling
Resume score status
Skill match visualization
PDF report generation
Results page UI improvements

This approach makes it easier to track the development process and maintain the project.

Future Enhancements

The project can be improved further by adding:

Advanced NLP based resume analysis
More job roles
Machine learning based job prediction
Semantic skill matching
Experience level detection
Resume keyword optimization
ATS compatibility score
Resume section analysis
User login and profile management
Database integration
Cloud deployment
Multiple resume comparison
Job recommendation system
Integration with job portals
AI-generated resume improvement suggestions
Project Goal

The main goal of ResumeAI is to make resume analysis faster and easier for job seekers.

Instead of manually comparing a resume with a job description, the application provides an automated analysis and clearly shows what matches, what is missing, and what can be improved.

Conclusion

ResumeAI demonstrates how Python, Flask, resume processing, skill matching, and web technologies can be combined to build a practical AI-based career assistance application.

The project can be further extended into a complete AI-powered career platform with resume optimization, job recommendations, ATS analysis, and personalized career suggestions.

## Future Enhancements

The project can be extended with the following features:

- AI-powered resume improvement suggestions
- Job description matching and recommendation
- Resume keyword optimization for ATS systems
- Support for additional resume file formats
- User-friendly analysis history and report management
## Project Highlights

ResumeAI is built to simplify the resume screening process by comparing a candidate's resume with a specific job description.

Key highlights:

- Automated resume analysis using Python and Flask
- PDF and DOCX resume processing
- Job-role and skill detection
- Resume-to-job skill comparison
- Missing skill identification
- Overall resume scoring
- Strengths and weaknesses analysis
- Downloadable PDF analysis reports
- Responsive web interface
- Clear validation and error handling


## Prerequisites

Before running ResumeAI, make sure the following are installed:

- Python 3.x
- Git
- VS Code or another code editor
- A modern web browser
- pip package manager


## Application Workflow

The ResumeAI analysis workflow can be summarized as:

Resume Upload
        ?
File Validation
        ?
Resume Text Extraction
        ?
Job Description Analysis
        ?
Job Role Detection
        ?
Required Skill Extraction
        ?
Resume Skill Detection
        ?
Skill Comparison
        ?
Resume Score Calculation
        ?
Strengths & Weaknesses Analysis
        ?
Recommendations
        ?
PDF Report Generation


## Analysis Metrics

ResumeAI evaluates a resume using several important metrics:

### Skill Match

Measures how many of the skills required by the job description are present in the resume.

### Resume Score

Provides an overall score based on factors such as:

- Skill match
- Projects
- Education
- Experience or internship information

### Matched Skills

Lists the skills that are found both in the job requirements and the resume.

### Missing Skills

Identifies important skills mentioned in the job description but not found in the resume.

### Strengths

Highlights positive aspects of the resume based on the analysis.

### Weaknesses

Identifies areas where the resume may need improvement.

### Recommendations

Provides suggestions that can help the candidate improve the resume for the selected job role.


## Technology Architecture

ResumeAI uses a simple web application architecture:

### Frontend Layer

- HTML provides the page structure
- CSS handles styling and responsive design
- JavaScript provides interactive features
- Jinja2 templates connect the frontend with Flask

### Backend Layer

- Flask handles HTTP requests and application routing
- Python manages the application logic
- Resume processing services extract text from uploaded files
- AI analysis services compare resume content with job requirements

### Analysis Layer

The analysis process combines:

- Resume text extraction
- Job description processing
- Skill detection
- Skill comparison
- Resume scoring
- Recommendation generation

### Reporting Layer

The final analysis is presented on the results page and can also be exported as a downloadable PDF report.

