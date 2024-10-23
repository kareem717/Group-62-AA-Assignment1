import re
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')

# mock db as a dict
mock_db = {
    'users': []
}

def find_user_by_email(email):
    return next((user for user in mock_db['users'] if user['email'] == email), None)

def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,63}$"
    if re.match(email_regex, email):
        locale, domain_tld = email.split('@')
        domain, tld = domain_tld.split('.')
        if 1 <= len(locale) <= 64 and 1 <= len(domain) <= 191 and 2 <= len(tld) <= 63 and 6 <= len(email) <= 320:
            return True
    return False

def is_valid_password(password):
    return 6 <= len(password) <= 320

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('index.html', user_input=user_input)
    return render_template('index.html', user_input=None)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # handle form submission
        email = request.form.get('email')
        password = request.form.get('password')
        terms_accepted = request.form.get('terms')

        # validate email
        if not email or not is_valid_email(email):
            return "Invalid email", 400

        # Validate password
        if not password or not is_valid_password(password):
            if len(password) < 6:
                return "Password too short", 400
            if len(password) > 320:
                return "Password too long", 400

        if not terms_accepted:
            return "Please accept the terms and conditions.", 400

        if find_user_by_email(email):
            return "User already exists.", 400

        new_user = {'email': email, 'password': password}
        mock_db['users'].append(new_user)

        # Redirect to the login page after successful signup
        return redirect(url_for('login'))

    # Handle GET request - render the signup page
    return render_template('sign-up.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'message': 'Email and password are required.'}), 400

        user = find_user_by_email(email)
        if not user or user['password'] != password:
            return jsonify({'message': 'Invalid email or password.'}), 401

        # redirect to the index page after successful login
        return redirect(url_for('index'))

    # handle GET request - render the login page
    return render_template('login.html')

@app.route('/flight-search')
def search_flights():
    return render_template('flight-search.html')

if __name__ == '__main__':
    app.run(debug=False , port=5002)