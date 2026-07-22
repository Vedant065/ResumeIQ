
import os
from fastapi import APIRouter, UploadFile, File, Form
from app.services.job_match import compare_resume_with_job
from app.services.parser import extract_text
from app.services.ats import calculate_ats_score
from app.services.gemini import analyze_resume

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    job_description: str = Form("")
    ):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract resume text
    resume_text = extract_text(file_path)

    # Calculate ATS score
    ats = calculate_ats_score(resume_text)
    
    job_match = compare_resume_with_job(
        resume_text,
        job_description
    )
    # Get AI feedback (don't fail if Gemini has an issue)
    try:
        ai_feedback = analyze_resume(resume_text)
    except Exception as e:
        print("Gemini Error:", e)
        ai_feedback = "AI feedback is currently unavailable."

    # Return response
    return {
        "filename": file.filename,
        "ats_score": ats["score"],
        "keywords_found": ats["keywords"],
        "strengths": ats["strengths"],
        "missing_keywords": ats["missing_keywords"],
        "suggestions": ats["suggestions"],
        "section_analysis": ats["section_analysis"],
        "resume_preview": resume_text[:700],
        "ai_feedback": ai_feedback,

        # Job Match
        "match_score": job_match["match_score"],
        "matched_skills": job_match["matched_skills"],
        "missing_skills": job_match["missing_skills"],
    }