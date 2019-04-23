from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def signup_form():
    return render_template('signup.html')


def check_length(nput):
    length = len(nput)
    return length
    #check if input == less than three characters, or more than twenty.

def check_spaces(nput):
    for i in nput:
        if i == " ":
            return "error"

def first_name_check(nput):
    if check_length(nput) <= 1:
        return "Field must contain 2 of more characters!"
    if check_spaces(nput) == "error":
        return "Field must not contain spaces!"
    return ""

def last_name_check(nput):
    if check_length(nput) <= 1:
        return "Field must contain 2 of more characters!"
    if check_spaces(nput) == "error":
        return "Field must not contain spaces!"
    return ""
def user_name_check(user_name):
    if check_spaces(user_name) == "error":
        return "Field must not contain spaces!"
    if check_length(user_name) < 3 or check_length(user_name) > 20:
        return "Field must be between 3 and 20 characters!"
    return ""

def email_address_check(email_address):
    A1 = 0
    D1 = 0
    if check_spaces(email_address) == "error":
        return "Email must not contain spaces!" 
    for i in email_address:
        if i == "@":
            A1 = A1 + 1
        if i == ".":
            D1 = D1 + 1
    if A1 == 1 and D1 == 1:
        return ""
    else:
        return "Invalid email address!" 
    if check_length(email_address) < 3:
        return "Email must be more than three characters!"
     #check for single '.' and '@' symbols

def password_check(password):
    if check_spaces(password) == "error":
        return "Password must not contain spaces!"
    if check_length(password) < 3 or check_length(password) > 20:
        return "Password must be between 3 and 20 characters!"
    return ""

def confirm_password_check(confirm_password,password):
    if confirm_password != password:
        return "Both passwords do not match!"
    return ""  
    #compare both passwords
    
def field_empty(field):
    if field == "":
        return True
    return False
    #check for empty field
@app.route('/success')
def successful_login():
    return render_template('success.html')

@app.route('/', methods=['POST'])
def signup_verif():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email_address = request.form['email_address']
    user_name = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    firsname_valid_message = first_name_check(first_name)
    lasname_valid_message =  last_name_check(last_name)
    password_valid_message = password_check(password)
    pasword_confirm_message= confirm_password_check(confirm_password,password)
    is_email_address_confirmed = email_address_check(email_address)
    user_name_valid_message = user_name_check(user_name)
    all_errors = [firsname_valid_message, lasname_valid_message, password_valid_message, pasword_confirm_message, is_email_address_confirmed, user_name_valid_message]

    for error_text in all_errors:
        if error_text != "":
            return render_template('signup.html', first_name_error = firsname_valid_message, last_name_error = lasname_valid_message, user_name_error= user_name_valid_message,  password_error = password_valid_message, confirm_password_error = pasword_confirm_message, email_address_error = is_email_address_confirmed)
    return redirect('/success')

        
    
app.run()