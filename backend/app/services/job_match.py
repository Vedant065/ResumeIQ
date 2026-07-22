import re

COMMON_SKILLS = [
    "python",
    "java",
    "c++",
    "react",
    "node",
    "fastapi",
    "flask",
    "docker",
    "kubernetes",
    "git",
    "aws",
    "azure",
    "sql",
    "mongodb",
    "mysql",
    "html",
    "css",
    "javascript",
    "typescript",
    "machine learning",
]


def compare_resume_with_job(resume_text: str, job_description: str):
    resume = resume_text.lower()
    job = job_description.lower()

    matched = []
    missing = []

    for skill in COMMON_SKILLS:
        if skill in job:
            if skill in resume:
                matched.append(skill)
            else:
                missing.append(skill)

    total = len(matched) + len(missing)

    if total == 0:
        score = 100
    else:
        score = int((len(matched) / total) * 100)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
    }