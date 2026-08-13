import re


JOB_SKILLS = {

    "python developer": [
        "python",
        "flask",
        "django",
        "fastapi",
        "pandas",
        "numpy",
        "sql",
        "rest api",
        "git"
    ],

    "java developer": [
        "java",
        "spring",
        "spring boot",
        "hibernate",
        "maven",
        "junit",
        "jdbc",
        "rest api",
        "sql",
        "git"
    ],

    "web developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "sql",
        "git"
    ],

    "data scientist": [
        "python",
        "pandas",
        "numpy",
        "machine learning",
        "scikit-learn",
        "sql",
        "tensorflow",
        "power bi"
    ],

    "machine learning engineer": [
        "python",
        "machine learning",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "numpy",
        "pandas",
        "sql",
        "git"
    ],

    "data analyst": [
        "python",
        "pandas",
        "numpy",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "matplotlib",
        "statistics",
        "git"
    ],

    "frontend developer": [
        "html",
        "css",
        "javascript",
        "react",
        "typescript",
        "bootstrap",
        "git"
    ],

    "backend developer": [
        "python",
        "java",
        "node.js",
        "django",
        "flask",
        "spring boot",
        "rest api",
        "sql",
        "mongodb",
        "git"
    ],

    "full stack developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "python",
        "java",
        "sql",
        "mongodb",
        "git"
    ],

    "sql developer": [
        "sql",
        "mysql",
        "postgresql",
        "oracle",
        "database",
        "pl/sql",
        "jdbc",
        "git"
    ]
}


def skill_exists(skill, text):
    """
    Checks whether a skill exists in the provided text.
    Uses word boundaries for more accurate matching.
    """

    text = text.lower()
    skill = skill.lower()

    escaped_skill = re.escape(skill)

    if re.search(r"\b" + escaped_skill + r"\b", text):
        return True

    return False


def extract_job_skills(job_description):

    job_text = job_description.lower()

    detected_skills = []

    for skill_list in JOB_SKILLS.values():

        for skill in skill_list:

            if skill_exists(skill, job_text):

                if skill not in detected_skills:

                    detected_skills.append(skill)

    return detected_skills


def detect_job_type(job_description):

    job_text = job_description.lower()

    best_job = None
    best_count = 0

    for job_name, skills in JOB_SKILLS.items():

        count = 0

        for skill in skills:

            if skill_exists(skill, job_text):

                count += 1

        if count > best_count:

            best_count = count
            best_job = job_name

    return best_job


def analyze_resume(resume_text, job_description):

    resume_text_lower = resume_text.lower()

    detected_job = detect_job_type(job_description)

    required_skills = []

    if detected_job:

        required_skills = JOB_SKILLS[detected_job]

    else:

        required_skills = extract_job_skills(job_description)

    found_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill_exists(skill, resume_text_lower):

            found_skills.append(skill)

        else:

            missing_skills.append(skill)

    if len(required_skills) > 0:

        skill_match = (
            len(found_skills) /
            len(required_skills)
        ) * 100

    else:

        skill_match = 0

    skill_match = round(skill_match)

    strengths = []

    weaknesses = []

    recommendations = []

    if found_skills:

        strengths.append(
            f"Your resume contains {len(found_skills)} "
            f"of the {len(required_skills)} skills required "
            f"for this job."
        )

    if "project" in resume_text_lower:

        strengths.append(
            "Projects are included in the resume."
        )

    if "education" in resume_text_lower:

        strengths.append(
            "Education information is included."
        )

    if (
        "experience" in resume_text_lower
        or "internship" in resume_text_lower
    ):

        strengths.append(
            "Experience or internship information is included."
        )

    if missing_skills:

        weaknesses.append(
            "Some important skills required for this job "
            "are missing from the resume."
        )

    if "project" not in resume_text_lower:

        weaknesses.append(
            "Projects section is missing or unclear."
        )

    if (
        "experience" not in resume_text_lower
        and "internship" not in resume_text_lower
    ):

        weaknesses.append(
            "Professional experience or internship "
            "information is limited."
        )

    if missing_skills:

        recommendations.append(
            "Consider adding the missing skills only if "
            "you genuinely have experience with them."
        )

    recommendations.append(
        "Customize your resume according to the specific job description."
    )

    recommendations.append(
        "Use measurable achievements in your projects "
        "and experience sections."
    )

    recommendations.append(
        "Keep job-specific keywords relevant and natural."
    )

    overall_score = skill_match

    if "project" in resume_text_lower:

        overall_score += 5

    if "education" in resume_text_lower:

        overall_score += 5

    if (
        "experience" in resume_text_lower
        or "internship" in resume_text_lower
    ):

        overall_score += 5

    overall_score = min(
        round(overall_score),
        100
    )

    return {

        "job_description": job_description,

        "detected_job": detected_job,

        "resume_score": overall_score,

        "skill_match": skill_match,

        "skills": found_skills,

        "required_skills": required_skills,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "missing_skills": missing_skills,

        "recommendations": recommendations
    }