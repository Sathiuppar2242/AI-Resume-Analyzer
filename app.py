from flask import Flask, render_template, request
import os

from services.resume_parser import extract_resume_text
from services.ai_analyzer import analyze_resume


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")

    job_description = request.form.get("job_description", "").strip()


    # Resume validation

    if not resume or resume.filename == "":

        return render_template(
            "index.html",
            error="Please upload your resume."
        )


    # File type validation

    if not allowed_file(resume.filename):

        return render_template(
            "index.html",
            error="Invalid file type. Please upload a PDF or DOCX file."
        )


    # Job description validation

    if not job_description:

        return render_template(
            "index.html",
            error="Please enter the complete job description."
        )


    # Save uploaded resume

    filename = resume.filename

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    resume.save(filepath)


    try:

        # Extract resume text

        resume_text = extract_resume_text(filepath)


        # AI analysis

        analysis = analyze_resume(
            resume_text,
            job_description
        )


        return render_template(
            "result.html",
            analysis=analysis,
            resume_name=filename
        )


    except Exception as e:

        return render_template(
            "index.html",
            error=f"Error analyzing resume: {str(e)}"
        )


if __name__ == "__main__":

    app.run(debug=True)