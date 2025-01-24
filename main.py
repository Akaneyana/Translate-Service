from flask import Flask, render_template, request, redirect, url_for, session
from backend.databaseConnection import register_user, place_order, verify_user_credentials
import os

template_path = os.path.join('frontend', 'templates')
static_path = os.path.join('frontend', 'static')

app = Flask(
    __name__,
    template_folder=template_path,
    static_folder=static_path
)

app.secret_key = os.getenv("FLASK_SECRET_KEY", "mysecretkey")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user_id = verify_user_credentials(email, password)
        if user_id:
            session['user_id'] = user_id
            message = "Logged in successfully!"
            return render_template('index.html', message=message)
        else:
            message = "Invalid email or password."

    return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    message = "Logged out successfully."
    return render_template('index.html', message=message)


@app.route('/order', methods=['GET', 'POST'])
def order():
    if 'user_id' not in session:
        message = "You must log in to place an order."
        return render_template('message.html', message=message)

    message = None
    if request.method == 'POST':
        user_id = session['user_id']
        Book = request.form['Book']
        Language = request.form['Language']
        Note = request.form['Note']

        try:
            place_order(user_id, Book, Language, Note)  # Call the function from databaseConnection
            message = "Order placed successfully!"
        except Exception as e:
            message = f"An error occurred: {e}"

    return render_template('order.html', message=message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        try:
            register_user(first_name, last_name, password, email)
            message = "Registration successful! Please log in."
        except Exception as e:
            message = f"Error during registration: {str(e)}"

        return render_template('register.html', message=message)

    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
