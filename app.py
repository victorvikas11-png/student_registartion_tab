from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Capturing the new fields
    name = request.form.get('name')
    roll = request.form.get('roll')
    email = request.form.get('email')    # New
    phone = request.form.get('phone')    # New
    course = request.form.get('course')  # New
    
    # Printing to the Spyder console so you can see it working
    print(f"--- New Submission ---")
    print(f"Name: {name}\nRoll: {roll}\nEmail: {email}\nPhone: {phone}\nCourse: {course}")
    
    return f"""
    <h1>Submission Received!</h1>
    <p>Thank you, {name}. We have registered you for the <b>{course}</b> course.</p>
    <a href="/">Go Back</a>
    """

if __name__ == '__main__':
    app.run(port=5000)