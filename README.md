🧠 Resume Analyzer  
A smart and simple tool that automatically analyzes resumes and extracts key information such as name, email, phone number, skills, and experience using Python, **Flask, and **NLP (Natural Language Processing).  



## 🚀 Features  
- 📂 Upload resumes in PDF or DOCX format  
- 🧾 Automatically extracts Name, Email, Phone, Skills, and Experience  
- 🧠 Uses NLP to identify relevant keywords and skills  
- 🌐 Clean and simple Flask-based web interface  
- ⚙ Easy to customize and integrate with other apps  


## 🛠 Tech Stack  
| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Framework | Flask |
| Libraries | PyPDF2, docx2txt, Spacy, ResumeParser |
| Frontend | HTML, CSS |
| Tools | Git, VS Code |



##  Installation & Setup  
Follow these steps to set up and run the project on your local machine 👇  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/ramadasusiri2806-boop/resume-analyzer.git

2️⃣ Navigate to the Project Folder
bash
Copy code
cd resume-analyzer

3️⃣ Create and Activate a Virtual Environment
Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
macOS/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate

4️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt

5️⃣ Run the Flask Application
bash
Copy code
python app.py
Now open your browser and go to 👉 http://127.0.0.1:5000/

🖼 Demo
Here’s an example of how the app works 👇
Upload Resume → Extract Info → Display Output
makefile
Copy code
Name: john  
Email: johnexample00@email.com 
Phone: +91XXXXXXXXXX  
Skills: Python, Data Science, Flask, Machine Learning  
Experience: 1 year internship
(You can also add a screenshot here later, like this)
markdown
Copy code
![Resume Analyzer Demo](demo.png)
📂 Project Structure
resume-analyzer/
│
├── app.py                # Main Flask app (handles routes and file uploads)
├── analyzer.py           # Resume analysis logic (text extraction & NLP)
├── templates/            # HTML templates
│   ├── index.html        # Upload page
│   └── result.html       # Display extracted results
├── static/               # CSS, JS, and images
├── uploads/              # Uploaded resumes
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
🧭 Future Enhancements
Add AI-based resume ranking
Support for multiple resumes at once
Export results to Excel/CSV
Improve accuracy using pre-trained NLP models
📄 License
This project is licensed under the MIT License.
🙌 Acknowledgements
Inspired by open-source NLP resume parsers and AI-based hiring tools.
GitHub: @ramadasusiri2806-boop
