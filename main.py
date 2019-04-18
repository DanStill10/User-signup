from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def signup():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email_address = request.args.get('email_address')
    password = request.args.get('password')
    confirm_password = request.args.get('confirm_password')
    return render_template('signup.html')

app.run()