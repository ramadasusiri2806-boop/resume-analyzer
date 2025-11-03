from flask import Flask, render_template, request
import os
import csv
from analyzer import analyze_resume

# --- Initialize Flask app ---
app = Flask(__name__)

# --- Configure upload folder ---
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# --- Home route ---
@app.route("/")
def home():
    return render_template("index.html")


# --- Upload & Analyze route ---
@app.route("/upload", methods=["POST"])
def upload_file():
    if "resume" not in request.files:
        return "No file uploaded."

    file = request.files["resume"]
    role = request.form.get("role")

    if file.filename == "":
        return "No file selected."

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Analyze resume
    result = analyze_resume(filepath, role)

    # Save to CSV history
    with open("resume_history.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            file.filename,
            role,
            result["score"],
            result["found_skills"],
            result["missing_skills"],
            "; ".join(result["suggestions"])
        ])

    return render_template("result.html", result=result, role=role)


# --- Run the Flask server ---
if __name__ == "__main__":
    app.run(debug=True)
