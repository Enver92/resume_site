from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Experience
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Education
@app.route('/education')
def education():
    return render_template('education.html')

# Contacts
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()
