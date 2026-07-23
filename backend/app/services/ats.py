import re
from collections import Counter

# ==========================================================
# TECHNICAL KEYWORDS
# ==========================================================

KEYWORDS = [

    # Languages
    "python","java","c","c++","c#","javascript","typescript",

    # Web
    "html","css","bootstrap","tailwind","react","reactjs",
    "angular","vue","vite","nextjs",

    # Backend
    "node","nodejs","express","fastapi","flask","django",

    # Database
    "sql","mysql","postgresql","mongodb","firebase",

    # Cloud
    "aws","azure","gcp","docker","kubernetes","render",

    # AI
    "machine learning","deep learning","artificial intelligence",
    "nlp","computer vision","tensorflow","keras","pytorch",
    "scikit","opencv",

    # Development
    "git","github","rest api","api","jwt","oauth","authentication",

    # CS Fundamentals
    "data structures","algorithms","oop","operating system",
    "computer networks","dbms",

    # Soft Skills
    "leadership","teamwork","communication",
    "problem solving","critical thinking"

]

# ==========================================================
# ACTION VERBS
# ==========================================================

ACTION_VERBS = [

    "developed",
    "built",
    "created",
    "implemented",
    "designed",
    "optimized",
    "improved",
    "managed",
    "led",
    "integrated",
    "engineered",
    "automated",
    "deployed",
    "tested",
    "analyzed",
    "configured",
    "maintained",
    "debugged",
    "collaborated",
    "achieved"

]

# ==========================================================
# COMMON RESUME SECTIONS
# ==========================================================

SECTION_KEYWORDS = {

    "Education":[
        "education",
        "academic"
    ],

    "Skills":[
        "skills",
        "technical skills",
        "core competencies"
    ],

    "Projects":[
        "projects",
        "project"
    ],

    "Experience":[
        "experience",
        "internship",
        "work experience",
        "professional experience"
    ],

    "Certifications":[
        "certification",
        "certifications",
        "licenses"
    ],

    "Achievements":[
        "achievements",
        "awards"
    ]

}

# ==========================================================
# CONTACT REGEX
# ==========================================================

EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

PHONE_REGEX = r"(\+?\d[\d\s\-]{9,15})"

LINKEDIN_REGEX = r"linkedin\.com"

GITHUB_REGEX = r"github\.com"

PORTFOLIO_REGEX = r"(portfolio|behance|dribbble|vercel|netlify)"

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def count_keywords(text):

    text = text.lower()

    found = []

    for keyword in KEYWORDS:

        if keyword in text:

            found.append(keyword)

    return found


def count_action_verbs(text):

    text = text.lower()

    count = 0

    for verb in ACTION_VERBS:

        count += len(re.findall(r"\b"+re.escape(verb)+r"\b",text))

    return count


def count_numbers(text):

    return len(
        re.findall(
            r"\d+%|\d+\+|\d+\.\d+|\d+",
            text
        )
    )


def detect_sections(text):

    text=text.lower()

    detected={}

    for section,names in SECTION_KEYWORDS.items():

        detected[section]=False

        for name in names:

            if name in text:

                detected[section]=True
                break

    return detected


def get_word_count(text):

    return len(text.split())


def unique_keyword_count(text):

    return len(set(count_keywords(text)))
# ==========================================================
# CONTACT INFORMATION SCORE (5 Marks)
# ==========================================================

def score_contact_information(text):

    score = 0
    strengths = []
    suggestions = []

    if re.search(EMAIL_REGEX, text):
        score += 1
        strengths.append("Professional email address found.")
    else:
        suggestions.append("Add a professional email address.")

    if re.search(PHONE_REGEX, text):
        score += 1
        strengths.append("Phone number found.")
    else:
        suggestions.append("Add a phone number.")

    if re.search(LINKEDIN_REGEX, text.lower()):
        score += 1
        strengths.append("LinkedIn profile included.")
    else:
        suggestions.append("Include your LinkedIn profile.")

    if re.search(GITHUB_REGEX, text.lower()):
        score += 1
        strengths.append("GitHub profile included.")
    else:
        suggestions.append("Include your GitHub profile.")

    if re.search(PORTFOLIO_REGEX, text.lower()):
        score += 1
        strengths.append("Portfolio website found.")

    return {
        "score": score,
        "strengths": strengths,
        "suggestions": suggestions
    }


# ==========================================================
# RESUME STRUCTURE SCORE (15 Marks)
# ==========================================================

def score_resume_structure(text):

    sections = detect_sections(text)

    score = 0
    strengths = []
    suggestions = []
    analysis = []

    mandatory = [
        "Education",
        "Skills",
        "Projects",
        "Experience"
    ]

    optional = [
        "Certifications",
        "Achievements"
    ]

    # Mandatory Sections
    for section in mandatory:

        present = sections.get(section, False)

        analysis.append({
            "name": section,
            "present": present
        })

        if present:
            score += 3
        else:
            suggestions.append(
                f"Missing '{section}' section."
            )

    # Optional Sections
    for section in optional:

        present = sections.get(section, False)

        analysis.append({
            "name": section,
            "present": present
        })

        if present:
            score += 1.5

    if score >= 13:
        strengths.append(
            "Resume contains an excellent structure."
        )

    elif score >= 10:
        strengths.append(
            "Resume has a good overall structure."
        )

    else:
        suggestions.append(
            "Organize the resume using standard ATS-friendly headings."
        )

    return {
        "score": round(score, 1),
        "strengths": strengths,
        "suggestions": suggestions,
        "analysis": analysis
    }


# ==========================================================
# READABILITY SCORE (5 Marks)
# ==========================================================

def score_readability(text):

    score = 0

    strengths = []

    suggestions = []

    words = get_word_count(text)

    if 300 <= words <= 650:
        score += 3
        strengths.append(
            "Resume length is ideal."
        )

    elif 220 <= words < 300:
        score += 2

    elif words > 650:
        score += 1
        suggestions.append(
            "Reduce unnecessary content."
        )

    else:
        score += 1
        suggestions.append(
            "Expand project and experience descriptions."
        )

    lines = text.splitlines()

    non_empty = [
        line.strip()
        for line in lines
        if line.strip()
    ]

    if len(non_empty) >= 20:
        score += 2
        strengths.append(
            "Good content distribution."
        )
    else:
        suggestions.append(
            "Resume looks sparse. Add more meaningful content."
        )

    return {
        "score": score,
        "strengths": strengths,
        "suggestions": suggestions
    }
    # ==========================================================
# SKILLS & TECHNICAL KEYWORD SCORE (20 Marks)
# ==========================================================

def score_skills(text):

    text_lower = text.lower()

    strengths = []
    suggestions = []

    keywords_found = []
    missing_keywords = []

    # Find unique technical keywords
    for keyword in KEYWORDS:

        if re.search(r"\b" + re.escape(keyword) + r"\b", text_lower):
            keywords_found.append(keyword)
        else:
            missing_keywords.append(keyword)

    unique_count = len(keywords_found)

    # -----------------------------
    # Score Calculation
    # -----------------------------

    if unique_count >= 20:
        score = 20

    elif unique_count >= 17:
        score = 18

    elif unique_count >= 14:
        score = 16

    elif unique_count >= 11:
        score = 14

    elif unique_count >= 8:
        score = 11

    elif unique_count >= 5:
        score = 8

    elif unique_count >= 3:
        score = 5

    else:
        score = 2

    # -----------------------------
    # Diversity Bonus
    # -----------------------------

    categories = 0

    if any(k in keywords_found for k in [
        "python","java","c","c++","c#","javascript","typescript"
    ]):
        categories += 1

    if any(k in keywords_found for k in [
        "react","angular","vue","html","css","tailwind"
    ]):
        categories += 1

    if any(k in keywords_found for k in [
        "fastapi","flask","django","node","express"
    ]):
        categories += 1

    if any(k in keywords_found for k in [
        "mysql","postgresql","mongodb","firebase"
    ]):
        categories += 1

    if any(k in keywords_found for k in [
        "aws","azure","docker","kubernetes","gcp","render"
    ]):
        categories += 1

    if categories >= 4:
        score += 2

    score = min(score, 20)

    # -----------------------------
    # Feedback
    # -----------------------------

    if score >= 18:

        strengths.append(
            "Excellent technical skill coverage."
        )

    elif score >= 14:

        strengths.append(
            "Good technical skill set."
        )

    elif score >= 10:

        strengths.append(
            "Moderate technical skill coverage."
        )

        suggestions.append(
            "Add more relevant technologies used in your projects."
        )

    else:

        suggestions.append(
            "Include more programming languages, frameworks, databases and tools."
        )

    return {

        "score": score,

        "keywords_found": keywords_found,

        "missing_keywords": missing_keywords,

        "strengths": strengths,

        "suggestions": suggestions

    }
    # ==========================================================
# ACTION VERB ANALYSIS
# ==========================================================

def score_action_verbs(text):

    strengths = []
    suggestions = []

    verb_count = count_action_verbs(text)

    if verb_count >= 15:

        score = 10
        strengths.append(
            "Excellent use of action verbs."
        )

    elif verb_count >= 10:

        score = 8
        strengths.append(
            "Good use of action verbs."
        )

    elif verb_count >= 6:

        score = 6

    elif verb_count >= 3:

        score = 4
        suggestions.append(
            "Use more action verbs like Developed, Built, Designed and Implemented."
        )

    else:

        score = 2
        suggestions.append(
            "Project descriptions should start with strong action verbs."
        )

    return {

        "score": score,

        "strengths": strengths,

        "suggestions": suggestions

    }
    # ==========================================================
# ACHIEVEMENT SCORE
# ==========================================================

def score_achievements(text):

    strengths = []
    suggestions = []

    numbers = count_numbers(text)

    if numbers >= 12:

        score = 10

        strengths.append(
            "Excellent quantified achievements."
        )

    elif numbers >= 8:

        score = 8

    elif numbers >= 5:

        score = 6

    elif numbers >= 3:

        score = 4

        suggestions.append(
            "Add more measurable achievements."
        )

    else:

        score = 2

        suggestions.append(
            "Use numbers like %, users, accuracy, time saved or performance improvements."
        )

    return {

        "score": score,

        "strengths": strengths,

        "suggestions": suggestions

    }
    # ==========================================================
# EXPERIENCE ANALYSIS (20 Marks)
# ==========================================================

def score_experience(text):

    text_lower = text.lower()

    strengths = []
    suggestions = []

    score = 0

    experience_words = [
        "experience",
        "internship",
        "intern",
        "software engineer",
        "developer",
        "research",
        "trainee",
        "worked",
        "employment",
        "professional experience"
    ]

    has_experience = any(word in text_lower for word in experience_words)

    if has_experience:

        score += 5

    else:

        suggestions.append(
            "Add internship or work experience."
        )

        return {
            "score": score,
            "strengths": strengths,
            "suggestions": suggestions
        }

    # ---------------------------------------
    # Action Verbs
    # ---------------------------------------

    verb_count = count_action_verbs(text)

    if verb_count >= 10:

        score += 5
        strengths.append(
            "Experience contains strong action verbs."
        )

    elif verb_count >= 5:

        score += 4

    elif verb_count >= 2:

        score += 2

    else:

        suggestions.append(
            "Describe your work using action verbs."
        )

    # ---------------------------------------
    # Quantified Achievements
    # ---------------------------------------

    number_count = count_numbers(text)

    if number_count >= 8:

        score += 5
        strengths.append(
            "Experience contains quantified achievements."
        )

    elif number_count >= 4:

        score += 4

    elif number_count >= 2:

        score += 2

    else:

        suggestions.append(
            "Mention achievements using numbers or percentages."
        )

    # ---------------------------------------
    # Technologies Used
    # ---------------------------------------

    tech_count = len(count_keywords(text))

    if tech_count >= 15:

        score += 5

    elif tech_count >= 10:

        score += 4

    elif tech_count >= 6:

        score += 3

    elif tech_count >= 3:

        score += 2

    else:

        suggestions.append(
            "Mention technologies used during internships or work."
        )

    if score >= 17:

        strengths.append(
            "Excellent professional experience."
        )

    elif score >= 13:

        strengths.append(
            "Good experience section."
        )

    return {

        "score": score,

        "strengths": strengths,

        "suggestions": suggestions

    }
    # ==========================================================
# PROJECT ANALYSIS (20 Marks)
# ==========================================================

def score_projects(text):

    text_lower = text.lower()

    strengths = []

    suggestions = []

    score = 0

    project_keywords = [

        "project",

        "developed",

        "built",

        "created",

        "implemented",

        "designed"

    ]

    project_occurrences = sum(
        text_lower.count(word)
        for word in project_keywords
    )

    if project_occurrences >= 6:

        score += 8

    elif project_occurrences >= 4:

        score += 6

    elif project_occurrences >= 2:

        score += 4

    else:

        suggestions.append(
            "Include at least two technical projects."
        )

    # ---------------------------------------
    # Technologies Used
    # ---------------------------------------

    technologies = len(count_keywords(text))

    if technologies >= 15:

        score += 6

    elif technologies >= 10:

        score += 5

    elif technologies >= 6:

        score += 4

    elif technologies >= 3:

        score += 2

    else:

        suggestions.append(
            "Mention technologies used in projects."
        )

    # ---------------------------------------
    # Quantified Results
    # ---------------------------------------

    numbers = count_numbers(text)

    if numbers >= 6:

        score += 3

    elif numbers >= 3:

        score += 2

    # ---------------------------------------
    # Action Verbs
    # ---------------------------------------

    verbs = count_action_verbs(text)

    if verbs >= 8:

        score += 3

    elif verbs >= 4:

        score += 2

    if score >= 16:

        strengths.append(
            "Projects are well described."
        )

    elif score >= 12:

        strengths.append(
            "Good project section."
        )

    else:

        suggestions.append(
            "Improve project descriptions with achievements and technologies."
        )

    return {

        "score": score,

        "strengths": strengths,

        "suggestions": suggestions

    }
    # ==========================================================
# ATS FORMATTING SCORE (10 Marks)
# ==========================================================

def score_formatting(text):

    strengths = []
    suggestions = []

    score = 0

    words = get_word_count(text)

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # Resume Length
    if 300 <= words <= 650:
        score += 2
        strengths.append("Resume length is ATS-friendly.")

    elif 220 <= words < 300:
        score += 1

    elif words > 700:
        suggestions.append("Resume is too lengthy.")

    else:
        suggestions.append("Resume is too short.")

    # Bullet Points
    bullet_count = len(
        re.findall(r"[•\-\*]", text)
    )

    if bullet_count >= 15:
        score += 2
        strengths.append("Good use of bullet points.")

    elif bullet_count >= 8:
        score += 1

    else:
        suggestions.append(
            "Use bullet points to improve readability."
        )

    # Contact Information
    if re.search(EMAIL_REGEX, text):
        score += 1

    if re.search(PHONE_REGEX, text):
        score += 1

    if re.search(LINKEDIN_REGEX, text.lower()):
        score += 1

    if re.search(GITHUB_REGEX, text.lower()):
        score += 1

    # Section Headings
    detected = detect_sections(text)

    if sum(detected.values()) >= 5:
        score += 2
        strengths.append("Resume uses proper section headings.")
    else:
        suggestions.append(
            "Use standard ATS section headings."
        )

    return {

        "score": min(score,10),

        "strengths": strengths,

        "suggestions": suggestions

    }
    # ==========================================================
# RESUME QUALITY SCORE (10 Marks)
# ==========================================================

def score_resume_quality(text):

    strengths = []

    suggestions = []

    score = 0

    word_count = get_word_count(text)

    action_verbs = count_action_verbs(text)

    numbers = count_numbers(text)

    technologies = len(count_keywords(text))

    # Word Count
    if 300 <= word_count <= 650:
        score += 2

    elif 220 <= word_count < 300:
        score += 1

    # Action Verbs
    if action_verbs >= 10:
        score += 3

    elif action_verbs >= 5:
        score += 2

    elif action_verbs >= 2:
        score += 1

    # Quantified Achievements
    if numbers >= 8:
        score += 3

    elif numbers >= 4:
        score += 2

    elif numbers >= 2:
        score += 1

    # Technology Diversity
    if technologies >= 15:
        score += 2

    elif technologies >= 10:
        score += 1

    if score >= 8:

        strengths.append(
            "Excellent resume quality."
        )

    elif score >= 6:

        strengths.append(
            "Good resume quality."
        )

    else:

        suggestions.append(
            "Improve descriptions with achievements and technologies."
        )

    return {

        "score": score,

        "strengths": strengths,

        "suggestions": suggestions

    }
    # ==========================================================
# FINAL RATING
# ==========================================================

def get_rating(score):

    if score >= 90:
        return "Excellent"

    elif score >= 80:
        return "Very Good"

    elif score >= 70:
        return "Good"

    elif score >= 60:
        return "Average"

    elif score >= 40:
        return "Needs Improvement"

    return "Poor"
# ==========================================================
# MAIN ATS FUNCTION
# ==========================================================

def calculate_ats_score(text: str):

    # -----------------------------
    # Run all scoring modules
    # -----------------------------

    contact = score_contact_information(text)

    structure = score_resume_structure(text)

    readability = score_readability(text)

    skills = score_skills(text)

    verbs = score_action_verbs(text)

    achievements = score_achievements(text)

    experience = score_experience(text)

    projects = score_projects(text)

    formatting = score_formatting(text)

    quality = score_resume_quality(text)

    # -----------------------------
    # Weighted Final Score
    # -----------------------------

    final_score = (
        contact["score"] +
        structure["score"] +
        readability["score"] +
        skills["score"] +
        verbs["score"] +
        achievements["score"] +
        experience["score"] +
        projects["score"] +
        formatting["score"] +
        quality["score"]
    )

    # Raw total is 115
    # Convert fairly to 100

    final_score = round((final_score / 115) * 100)

    # -----------------------------
    # Soft Normalization
    # -----------------------------

    if final_score > 95:
        final_score = 95

    elif final_score < 0:
        final_score = 0

    # -----------------------------
    # Merge Strengths
    # -----------------------------

    strengths = []

    for module in [
        contact,
        structure,
        readability,
        skills,
        verbs,
        achievements,
        experience,
        projects,
        formatting,
        quality
    ]:

        strengths.extend(module.get("strengths", []))

    strengths = list(dict.fromkeys(strengths))

    # -----------------------------
    # Merge Suggestions
    # -----------------------------

    suggestions = []

    for module in [
        contact,
        structure,
        readability,
        skills,
        verbs,
        achievements,
        experience,
        projects,
        formatting,
        quality
    ]:

        suggestions.extend(module.get("suggestions", []))

    suggestions = list(dict.fromkeys(suggestions))

    # -----------------------------
    # Missing Keywords
    # -----------------------------

    missing_keywords = skills["missing_keywords"][:10]

    # -----------------------------
    # Rating
    # -----------------------------

    rating = get_rating(final_score)

    # -----------------------------
    # ATS Verdict
    # -----------------------------

    if final_score >= 90:

        verdict = "Excellent ATS Compatibility"

    elif final_score >= 80:

        verdict = "Very Good ATS Compatibility"

    elif final_score >= 70:

        verdict = "Good ATS Compatibility"

    elif final_score >= 60:

        verdict = "Average ATS Compatibility"

    else:

        verdict = "Needs Improvement"

    # -----------------------------
    # Return
    # -----------------------------

    return {

        "score": final_score,

        "rating": rating,

        "verdict": verdict,

        "keywords": skills["keywords_found"],

        "missing_keywords": missing_keywords,

        "strengths": strengths,

        "suggestions": suggestions,

        "section_analysis": structure["analysis"],

        "breakdown": {

            "Contact": contact["score"],

            "Structure": structure["score"],

            "Readability": readability["score"],

            "Skills": skills["score"],

            "Action Verbs": verbs["score"],

            "Achievements": achievements["score"],

            "Experience": experience["score"],

            "Projects": projects["score"],

            "Formatting": formatting["score"],

            "Resume Quality": quality["score"]

        }

    }
