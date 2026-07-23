import re

KEYWORDS = [
    "python", "java", "c++", "sql", "react", "fastapi", "flask",
    "docker", "git", "aws", "azure", "machine learning",
    "tensorflow", "pytorch", "api", "mongodb", "mysql",
    "html", "css", "javascript",
]


def calculate_ats_score(text: str):
    text_lower = text.lower()

    score = 0

    strengths = []
    suggestions = []
    keywords_found = []
    missing_keywords = []

    # -----------------------------
    # Contact Information (5)
    # -----------------------------
    contact_score = 0

    if re.search(r"\S+@\S+\.\S+", text):
        contact_score += 2
    else:
        suggestions.append("Add a professional email address.")

    if re.search(r"\+?\d[\d\s\-]{8,}", text):
        contact_score += 3
    else:
        suggestions.append("Add a phone number.")

    score += contact_score

    # -----------------------------
    # Resume Sections (15)
    # -----------------------------
    sections = {
        "Education": "education" in text_lower,
        "Skills": "skills" in text_lower,
        "Projects": "project" in text_lower,
        "Experience": "experience" in text_lower,
        "Certifications": "certification" in text_lower,
    }

    section_analysis = []

    section_score = 0

    for name, present in sections.items():

        section_analysis.append({
            "name": name,
            "present": present
        })

        if present:
            section_score += 3
        else:
            suggestions.append(f"Add a {name} section.")

    score += section_score

    if section_score >= 12:
        strengths.append("Well-structured resume")

    # -----------------------------
    # Technical Keywords (25)
    # -----------------------------
    for keyword in KEYWORDS:

        if keyword in text_lower:
            keywords_found.append(keyword)
        else:
            missing_keywords.append(keyword)

    keyword_score = round(
        (len(keywords_found) / len(KEYWORDS)) * 25
    )

    score += keyword_score

    if keyword_score >= 18:
        strengths.append("Good technical skill coverage")
    else:
        suggestions.append(
            "Include more job-relevant technical skills."
        )

    # -----------------------------
    # Experience Quality (20)
    # -----------------------------
    experience_score = 0

    if "experience" in text_lower:

        experience_score += 8

        numbers = len(re.findall(r"\d+%|\d+\+|\d+", text))

        if numbers >= 8:
            experience_score += 12
            strengths.append(
                "Experience contains measurable achievements."
            )

        elif numbers >= 4:
            experience_score += 8

        else:
            experience_score += 4
            suggestions.append(
                "Add quantified achievements to your experience."
            )

    else:
        suggestions.append("Include work experience or internships.")

    score += experience_score

    # -----------------------------
    # Projects Quality (10)
    # -----------------------------
    project_score = 0

    project_count = text_lower.count("project")

    if project_count >= 3:
        project_score = 10
    elif project_count == 2:
        project_score = 8
    elif project_count == 1:
        project_score = 5
    else:
        suggestions.append(
            "Add at least two technical projects."
        )

    score += project_score

    # -----------------------------
    # Resume Length (5)
    # -----------------------------
    words = len(text.split())

    if 450 <= words <= 700:
        score += 5

    elif 300 <= words < 450:
        score += 4

    elif 200 <= words < 300:
        score += 3
        suggestions.append(
            "Expand project descriptions and achievements."
        )

    elif words > 700:
        score += 2
        suggestions.append(
            "Reduce resume length."
        )

    else:
        score += 1
        suggestions.append(
            "Resume is too short."
        )

    # -----------------------------
    # Final Adjustment
    # -----------------------------

    if score > 100:
        score = 100

    # Slight penalty if few keywords are found
    if len(keywords_found) < 8:
        score -= 5

    # Penalty for missing critical sections
    if not sections["Experience"]:
        score -= 5

    if not sections["Projects"]:
        score -= 5

    score = max(0, score)

    # -----------------------------
    # Rating
    # -----------------------------

    if score >= 90:
        strengths.append("Excellent ATS compatibility")

    elif score >= 75:
        strengths.append("Good ATS compatibility")

    elif score >= 60:
        suggestions.append(
            "Improve keyword optimization and quantify achievements."
        )

    else:
        suggestions.append(
            "Resume needs significant improvements for ATS."
        )

    return {
        "score": score,
        "keywords": keywords_found,
        "strengths": strengths,
        "missing_keywords": missing_keywords[:10],
        "suggestions": suggestions,
        "section_analysis": section_analysis,
    }