from flask import Flask, render_template, request, redirect, url_for
from backend.databaseConnection import register_user  # Import register_user function
import os

template_path = os.path.join('frontend', 'templates')
static_path = os.path.join('frontend', 'static')  # Correct static folder path

# Specify the correct folders
app = Flask(
    __name__,
    template_folder=template_path,  # HTML templates
    static_folder=static_path       # Static files
)

# Secret key for sessions (optional for this case)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "mysecretkey")

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # Call register_user from backend/databaseConnection.py
        try:
            register_user(first_name, last_name, password, email)
            # Pass the success message to the template
            return render_template('register.html', message="Registration successful! Please log in.")
        except Exception as e:
            # Pass the error message to the template
            return render_template('register.html', message=f"Error during registration: {str(e)}")

    # Render registration page on GET request
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
