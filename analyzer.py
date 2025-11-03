import fitz  # PyMuPDF
import re

def analyze_resume(file_path, role="data_analyst"):
    # --- Extract text from PDF ---
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    text_lower = text.lower()

    # --- Skill sets for each role ---
    skills = {
        "data_analyst": ["excel", "sql", "power bi", "tableau", "data visualization", "statistics", "data cleaning"],
        "data_scientist": ["python", "machine learning", "deep learning", "tensorflow", "pandas", "numpy", "matplotlib"],
        "web_developer": ["html", "css", "javascript", "react", "node", "express", "mongodb", "frontend", "backend"],
        "uiux_designer": ["figma", "adobe xd", "wireframe", "prototype", "user research", "visual design"],
        "cloud_engineer": ["aws", "azure", "gcp", "docker", "kubernetes", "terraform", "devops"],
        "cyber_security": ["network security", "firewall", "penetration testing", "ethical hacking", "encryption"]
    }

    # --- Skill match calculation ---
    keywords = skills.get(role, [])
    found = [k for k in keywords if k in text_lower]
    missing = [k for k in keywords if k not in text_lower]
    skill_score = int((len(found) / len(keywords)) * 100) if keywords else 0

    # --- Section presence checks ---
    experience_present = any(word in text_lower for word in ["intern", "experience", "worked", "developer", "engineer"])
    education_present = any(word in text_lower for word in ["b.tech", "bachelor", "university", "college", "degree"])
    project_present = any(word in text_lower for word in ["project", "developed", "created", "built", "implemented"])
    cert_present = any(word in text_lower for word in ["certification", "course", "award", "achievement"])
    cgpa_present = bool(re.search(r"\b\d\.\d\b", text))  # e.g., 8.5, 9.0
    email_present = bool(re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text))
    phone_present = bool(re.search(r"\b\d{10}\b", text))
    linkedin_present = "linkedin" in text_lower

    # --- Weighted scoring ---
    section_score = 0
    section_score += 15 if experience_present else 0
    section_score += 15 if education_present else 0
    section_score += 15 if project_present else 0
    section_score += 10 if cert_present else 0
    section_score += 10 if (email_present and phone_present and linkedin_present) else 0
    section_score += 5 if cgpa_present else 0

    total_score = min(100, int((skill_score * 0.4) + section_score))

    # --- Smart Suggestions ---
    suggestions = []

    if not cgpa_present:
        suggestions.append("🎓 Add your CGPA or percentage in the Education section.")
    if not (email_present and phone_present and linkedin_present):
        suggestions.append("📞 Include your email, phone number, and LinkedIn profile.")
    if not project_present:
        suggestions.append("💻 Mention at least one major project with technologies used.")
    if not cert_present:
        suggestions.append("📜 Add certifications or online courses to strengthen your profile.")
    if skill_score < 50:
        suggestions.append("⚙️ Add more key skills relevant to the selected role.")
    if total_score > 85:
        suggestions.append("🚀 Excellent resume! You’re job-ready.")
    if total_score <= 60:
        suggestions.append("📈 Improve your skills and add more project details to boost your score.")

    # --- Return result dictionary ---
    return {
        "score": total_score,
        "found_skills": ", ".join(found) if found else "None",
        "missing_skills": ", ".join(missing) if missing else "None",
        "experience": "✅ Found" if experience_present else "❌ Missing",
        "education": "✅ Found" if education_present else "❌ Missing",
        "projects": "✅ Found" if project_present else "❌ Missing",
        "certifications": "✅ Found" if cert_present else "❌ Missing",
        "contact": "✅ Found" if (email_present and phone_present and linkedin_present) else "❌ Missing",
        "cgpa": "✅ Found" if cgpa_present else "❌ Missing",
        "suggestions": suggestions
    }
