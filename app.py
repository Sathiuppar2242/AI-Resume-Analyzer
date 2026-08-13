from flask import Flask, render_template, request
import os

from services.resume_parser import extract_resume_text
from services.ai_analyzer import analyze_resume


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description")

    if not resume:
        return "Please upload a resume."

    if not job_description:
        return "Please enter the complete job description."

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(file_path)

    try:

        resume_text = extract_resume_text(file_path)

        if not resume_text.strip():
            return "Could not extract text from the resume."

        analysis = analyze_resume(
            resume_text,
            job_description
        )

        return render_template(
            "result.html",
            analysis=analysis,
            resume_name=resume.filename
        )

    except Exception as error:

        return f"Error analyzing resume: {error}"


if __name__ == "__main__":
    app.run(debug=True)