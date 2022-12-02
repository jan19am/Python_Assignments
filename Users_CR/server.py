from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key = 'qwerty'


#Route for displaying all users for db as variable all_users
@app.route('/users')
def display_all_users():

    return render_template('display.html', 
    all_users = User.get_all())


# relevant code snippet from server.py
# from user import User (for Modularization)
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')


@app.route('/users/new')
def user_form():
    
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)