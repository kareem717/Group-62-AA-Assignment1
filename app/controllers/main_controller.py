from flask import Blueprint, render_template, request
from models.user_input import UserInput

main_controller = Blueprint('main_controller', __name__)

@main_controller.route('/')
def index():
    return render_template('index.html')

@main_controller.route('/show', methods=['POST'])
def show():
    user_input = UserInput(request.form['user_input'])
    return f'You entered: {user_input.input_text}'