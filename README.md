# ResumeAI - AI Resume Analyzer

ResumeAI is an AI-powered web application that analyzes a candidate's resume against a specific job description.

The application evaluates the resume for relevant skills, calculates a resume score, identifies missing skills, highlights strengths and weaknesses, and provides recommendations to improve the resume for the selected job role.

## Project Overview

Finding out whether a resume is suitable for a particular job can take a lot of time.

ResumeAI simplifies this process by allowing users to upload their resume and enter a complete job description. The application analyzes both and generates a clear report showing how well the resume matches the job requirements.

The project is designed as a simple and user-friendly web application for students, job seekers, and developers.

## Key Features

* Upload resumes in PDF or DOCX format
* Validate uploaded resume files
* Enter complete job descriptions
* Automatically detect relevant job roles
* Identify required skills from job descriptions
* Extract skills from resumes
* Compare resume skills with job requirements
* Identify matched skills
* Identify missing skills
* Calculate skill match percentage
* Calculate overall resume score
* Analyze resume strengths
* Identify resume weaknesses
* Generate improvement recommendations
* Display animated skill-match progress
* Show an analysis loading screen
* Display clear validation and error messages
* Generate downloadable PDF analysis reports
* Responsive web interface
* Simple and user-friendly design

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

### Backend

* Python
* Flask

### Resume Processing

* PDF resume parsing
* DOCX resume parsing
* Regular expression-based skill matching
* Text extraction

### Development Tools

* Git
* GitHub
* Visual Studio Code
* Python Virtual Environment

## How ResumeAI Works

The application follows a simple resume analysis workflow:

1. User opens the ResumeAI website.
2. User uploads a resume.
3. The application validates the uploaded file.
4. User enters the complete job description.
5. Resume text is extracted.
6. The job description is analyzed.
7. The relevant job role is detected.
8. Required skills are identified.
9. Skills available in the resume are detected.
10. Resume skills are compared with required skills.
11. Skill match percentage is calculated.
12. Missing skills are identified.
13. Overall resume score is calculated.
14. Resume strengths and weaknesses are generated.
15. Improvement recommendations are generated.
16. Results are displayed on the analysis page.
17. User can download the analysis as a PDF report.

## Resume Score

ResumeAI calculates an overall resume score using multiple factors.

The score considers:

* Skill match
* Projects
* Education
* Experience or internship information

The final score is calculated on a scale of **0 to 100**.

## Skill Matching

ResumeAI compares the skills required by a job description with the skills found in the uploaded resume.

### Example

Suppose a Python Developer job requires:

* Python
* Flask
* Django
* SQL
* Git
* REST API

If the resume contains:

* Python
* Flask
* SQL
* Git

ResumeAI identifies the following:

### Matched Skills

* Python
* Flask
* SQL
* Git

### Missing Skills

* Django
* REST API

The application then calculates the skill match percentage based on the required skills.

## Supported Job Roles

The current version supports skill matching for several common roles:

* Python Developer
* Java Developer
* Web Developer
* Data Scientist
* Machine Learning Engineer
* Data Analyst
* Frontend Developer
* Backend Developer
* Full Stack Developer
* SQL Developer

## Analysis Metrics

### Skill Match

Measures how many skills required by the job description are available in the resume.

### Resume Score

Provides an overall score based on factors such as:

* Skill match
* Projects
* Education
* Experience or internship information

### Matched Skills

Lists the skills found both in the job requirements and the uploaded resume.

### Missing Skills

Identifies important skills mentioned in the job description but not found in the resume.

### Strengths

Highlights positive aspects of the resume based on the analysis.

### Weaknesses

Identifies areas where the resume may need improvement.

### Recommendations

Provides suggestions that can help candidates improve their resume for the selected job role.

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
├── .gitignore
├── requirements.txt
└── README.md
```

### Important Files

**`app.py`**

Main Flask application responsible for routing, file uploads, analysis requests, and generating results.

**`services/resume_parser.py`**

Responsible for extracting text from uploaded PDF and DOCX resumes.

**`services/ai_analyzer.py`**

Handles job-role detection, skill extraction, skill comparison, resume scoring, and recommendations.

**`templates/index.html`**

Contains the main resume upload and job-description input interface.

**`templates/result.html`**

Displays the generated resume analysis results.

**`static/`**

Contains CSS, JavaScript, and image assets used by the application.

**`uploads/`**

Used locally to temporarily store uploaded resumes during analysis.

## Installation

### Prerequisites

Before running ResumeAI, make sure the following are installed:

* Python 3.x
* Git
* VS Code or another code editor
* pip
* Modern web browser

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd AI-Resume-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

After activating the virtual environment, run:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000/
```

Open the address in your web browser.

## Using the Application

### Step 1 - Upload Resume

Upload your resume.

Supported formats:

* PDF
* DOCX

### Step 2 - Enter Job Description

Enter the complete job description.

Example:

```text
We are looking for a Python Developer with experience in
Python, Flask, Django, SQL, Git and REST API development.
```

### Step 3 - Analyze Resume

Click the **Analyze** button.

### Step 4 - Wait for Analysis

The application processes the resume and job description.

### Step 5 - View Results

The results page displays:

* Overall Resume Score
* Skill Match Percentage
* Required Skills
* Matched Skills
* Missing Skills
* Strengths
* Weaknesses
* Recommendations

### Step 6 - Download Report

The user can download the analysis as a PDF report for future reference.

## Error Handling

ResumeAI validates common user errors, including:

* Resume not uploaded
* Empty resume filename
* Unsupported file format
* Empty job description
* Invalid user input
* Resume processing errors
* Analysis errors

Clear error messages are displayed to help users understand and correct problems.

## PDF Analysis Report

ResumeAI provides a downloadable PDF analysis report.

The report can contain:

* Resume name
* Overall resume score
* Skill match percentage
* Required skills
* Matched skills
* Missing skills
* Strengths
* Weaknesses
* Recommendations

This allows users to save their analysis and review it later.

## Technology Architecture

ResumeAI follows a simple web application architecture.

### Frontend Layer

* HTML provides the page structure.
* CSS handles styling and responsive design.
* JavaScript provides interactive functionality.
* Jinja2 templates connect the frontend with Flask.

### Backend Layer

* Flask handles HTTP requests and application routing.
* Python manages application logic.
* Resume processing services extract text from uploaded documents.
* Analysis services compare resume content with job requirements.

### Analysis Layer

The analysis process includes:

* Resume text extraction
* Job description processing
* Job-role detection
* Skill detection
* Skill comparison
* Resume scoring
* Strength and weakness analysis
* Recommendation generation

### Reporting Layer

The final analysis is displayed on the results page and can also be exported as a downloadable PDF report.

## Application Workflow

```text
Resume Upload
      ↓
File Validation
      ↓
Resume Text Extraction
      ↓
Job Description Analysis
      ↓
Job Role Detection
      ↓
Required Skill Extraction
      ↓
Resume Skill Detection
      ↓
Skill Comparison
      ↓
Resume Score Calculation
      ↓
Strengths & Weaknesses Analysis
      ↓
Recommendations
      ↓
PDF Report Generation
```

## Security and Validation

ResumeAI includes basic validation measures to improve application reliability and prevent common upload-related issues.

The application validates:

* Allowed resume file formats
* Empty or invalid filenames
* Empty job descriptions
* Invalid user input
* Resume processing errors
* Analysis errors

Uploaded resumes are processed locally by the application during analysis.

For production deployment, additional security measures can be implemented, including:

* File size restrictions
* Secure filename handling
* Authentication and authorization
* Malware scanning
* Rate limiting
* Secure environment variables
* HTTPS configuration

## Example Analysis

For a Python Developer position, suppose the job description requires:

* Python
* Flask
* Django
* SQL
* Git
* REST API

If the uploaded resume contains:

* Python
* Flask
* SQL
* Git

ResumeAI can identify:

### Matched Skills

* Python
* Flask
* SQL
* Git

### Missing Skills

* Django
* REST API

The application then calculates the skill match percentage and provides an overall resume score along with strengths, weaknesses, and recommendations.

This helps candidates quickly understand how closely their resume matches a particular job description.

## Testing

The application should be tested using different resumes and job descriptions.

### Functional Tests

* Upload a valid PDF resume
* Upload a valid DOCX resume
* Test an unsupported file format
* Test an empty job description
* Test an empty resume
* Test different job roles
* Verify required skills
* Verify matched skills
* Verify missing skills
* Verify resume score calculation
* Verify the results page
* Verify PDF report generation

### Application Verification

Before publishing changes, verify:

* Flask starts successfully
* Resume processing works correctly
* PDF parsing works correctly
* DOCX parsing works correctly
* Skill matching works correctly
* Score calculation works correctly
* Error messages are displayed correctly
* PDF report downloads successfully
* Responsive UI works correctly

## Development Approach

ResumeAI was developed incrementally using version control and continuous testing.

The development process included:

1. Creating the Flask application foundation
2. Building the resume upload interface
3. Implementing PDF and DOCX processing
4. Adding job description analysis
5. Implementing skill matching
6. Adding resume scoring
7. Creating the results interface
8. Adding validation and error handling
9. Implementing PDF report generation
10. Improving the user interface
11. Testing application functionality
12. Updating project documentation

Git and GitHub were used throughout development to track changes and maintain different stages of the project.

## Project Benefits

ResumeAI provides several practical benefits:

* Saves time when comparing resumes with job descriptions
* Helps identify missing technical skills
* Provides a quick overview of resume-job compatibility
* Helps candidates understand their resume strengths and weaknesses
* Provides actionable improvement recommendations
* Supports both PDF and DOCX resumes
* Generates downloadable analysis reports
* Provides a simple web-based user experience
* Can be extended with advanced NLP and machine learning techniques

The project demonstrates how web development, Python programming, document processing, and AI-based analysis can be combined to solve a practical career-related problem.

## Current Limitations

The current version of ResumeAI has some limitations:

* Skill matching primarily depends on predefined skill patterns
* Advanced semantic understanding is limited
* Resume quality beyond the available analysis factors may not be fully evaluated
* Job-role detection may not cover every possible job title
* The application currently focuses on resume-to-job-description matching
* Authentication and user accounts are not implemented
* Analysis history is not stored in a database
* Production deployment configuration is not included

These limitations provide opportunities for future improvements using NLP, machine learning, semantic similarity models, databases, and cloud deployment.

## Future Enhancements

The project can be extended with the following features:

* Advanced NLP-based resume analysis
* AI-powered resume improvement suggestions
* Semantic skill matching
* Machine learning-based job prediction
* More job roles
* Experience-level detection
* Resume keyword optimization
* ATS compatibility analysis
* Resume section analysis
* User login and profile management
* Database integration
* Analysis history
* Multiple resume comparison
* Job recommendation system
* Integration with job portals
* Cloud deployment
* Personalized career suggestions

## Project Goal

The main goal of ResumeAI is to make resume analysis faster and easier for job seekers.

Instead of manually comparing a resume with a job description, the application provides an automated analysis that clearly shows:

* What matches
* What is missing
* What can be improved
* How well the resume fits the selected job

## Conclusion

ResumeAI demonstrates how Python, Flask, document processing, skill matching, and web technologies can be combined to build a practical AI-based career assistance application.

The project can be further developed into a complete AI-powered career platform with resume optimization, ATS analysis, job recommendations, semantic matching, and personalized career guidance.

## GitHub Development

The project was developed incrementally using Git and GitHub.

Development areas included:

* Project foundation
* Resume upload functionality
* Resume file validation
* PDF and DOCX processing
* Job description analysis
* Skill extraction
* Skill matching
* Resume scoring
* Results page
* Loading interface
* Error handling
* Skill-match visualization
* PDF report generation
* UI improvements
* Documentation updates

Version control helps maintain a clear development history and makes it easier to track improvements and future changes.

## License

This project is developed for educational and portfolio purposes.
