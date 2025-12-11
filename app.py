from flask import Flask, render_template, request
from resume_analyzer.extractor import extract_text_from_pdf
from resume_analyzer.score_engine import calculate_resume_score

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    jd = request.form['jd']

    text = extract_text_from_pdf(file)
    score, keywords_found = calculate_resume_score(text, jd)

    return render_template('index.html', score=score, found=keywords_found)

if __name__ == "__main__":
    app.run(debug=True)
