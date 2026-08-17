from flask import Flask, render_template, request, send_file
import os
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from services.resume_parser import extract_resume_text
from services.ai_analyzer import analyze_resume


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"pdf", "docx"}

MAX_FILE_SIZE = 5 * 1024 * 1024

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.errorhandler(413)
def request_entity_too_large(error):

    return render_template(
        "index.html",
        error="The uploaded resume is too large. Please upload a file smaller than 5 MB."
    ), 413


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    resume = request.files.get(
        "resume"
    )

    job_description = request.form.get(
        "job_description",
        ""
    ).strip()


    # Resume validation

    if not resume or resume.filename == "":

        return render_template(
            "index.html",
            error="Please upload your resume."
        )


    # File type validation

    if not allowed_file(
        resume.filename
    ):

        return render_template(
            "index.html",
            error="Invalid file type. Please upload a PDF or DOCX file."
        )


    # File size validation

    resume.seek(0, os.SEEK_END)

    file_size = resume.tell()

    resume.seek(0)


    if file_size > MAX_FILE_SIZE:

        return render_template(
            "index.html",
            error="Resume file is too large. Please upload a file smaller than 5 MB."
        )


    # Job description validation

    if not job_description:

        return render_template(
            "index.html",
            error="Please enter the complete job description."
        )


    if len(job_description) < 100:

        return render_template(
            "index.html",
            error="The job description is too short. Please provide at least 100 characters."
        )


    # Save uploaded resume

    filename = resume.filename

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )


    try:

        resume.save(
            filepath
        )


        # Extract resume text

        resume_text = extract_resume_text(
            filepath
        )


        if not resume_text or not resume_text.strip():

            return render_template(
                "index.html",
                error=(
                    "We couldn't extract readable text from your resume. "
                    "Please upload a valid PDF or DOCX file."
                )
            )


        # AI analysis

        analysis = analyze_resume(
            resume_text,
            job_description
        )


        if not analysis:

            return render_template(
                "index.html",
                error=(
                    "Resume analysis could not be completed. "
                    "Please try again with a valid resume and job description."
                )
            )


        return render_template(
            "result.html",
            analysis=analysis,
            resume_name=filename
        )


    except Exception as e:

        print(
            f"Analysis error: {type(e).__name__}: {str(e)}"
        )


        return render_template(
            "index.html",
            error=(
                "We couldn't complete the resume analysis right now. "
                "Please check your resume and job description and try again."
            )
        )


    finally:

        if os.path.exists(
            filepath
        ):

            try:

                os.remove(
                    filepath
                )

            except OSError:

                pass


@app.route(
    "/download-report",
    methods=["POST"]
)
def download_report():

    resume_name = request.form.get(
        "resume_name",
        "Resume"
    )


    resume_score = request.form.get(
        "resume_score",
        "0"
    )


    skill_match = request.form.get(
        "skill_match",
        "0"
    )


    skills = request.form.get(
        "skills",
        ""
    )


    missing_skills = request.form.get(
        "missing_skills",
        ""
    )


    strengths = request.form.get(
        "strengths",
        ""
    )


    weaknesses = request.form.get(
        "weaknesses",
        ""
    )


    recommendations = request.form.get(
        "recommendations",
        ""
    )


    pdf_buffer = BytesIO()


    pdf = canvas.Canvas(
        pdf_buffer,
        pagesize=A4
    )


    width, height = A4

    y = height - 50


    # Title

    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        50,
        y,
        "ResumeAI - Resume Analysis Report"
    )


    y -= 35


    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        y,
        f"Resume: {resume_name}"
    )


    y -= 30


    # Scores

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        y,
        "Analysis Summary"
    )


    y -= 25


    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        60,
        y,
        f"Overall Resume Score: {resume_score}%"
    )


    y -= 20


    pdf.drawString(
        60,
        y,
        f"Skill Match: {skill_match}%"
    )


    y -= 35


    # Helper function

    def add_section(
        title,
        content
    ):

        nonlocal y


        if y < 100:

            pdf.showPage()

            y = height - 50


        pdf.setFont(
            "Helvetica-Bold",
            14
        )

        pdf.drawString(
            50,
            y,
            title
        )


        y -= 22


        pdf.setFont(
            "Helvetica",
            10
        )


        if not content:

            content = "No information available."


        items = content.split("|")


        for item in items:

            item = item.strip()


            if not item:

                continue


            if y < 60:

                pdf.showPage()

                y = height - 50


            pdf.drawString(
                60,
                y,
                "• " + item[:100]
            )


            y -= 17


        y -= 15


    add_section(
        "Skills Found",
        skills
    )


    add_section(
        "Missing Skills",
        missing_skills
    )


    add_section(
        "Strengths",
        strengths
    )


    add_section(
        "Weaknesses",
        weaknesses
    )


    add_section(
        "Recommendations",
        recommendations
    )


    # Footer

    if y < 60:

        pdf.showPage()

        y = height - 50


    pdf.setFont(
        "Helvetica-Oblique",
        9
    )

    pdf.drawString(
        50,
        40,
        "Generated by ResumeAI - AI-Powered Resume Analyzer"
    )


    pdf.save()


    pdf_buffer.seek(0)


    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="ResumeAI_Analysis_Report.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )