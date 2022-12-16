# burgers.py
from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,session,flash


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


# Displays single user by Id
@app.route('/users/<int:id>')
def display_user(id):

    return render_template('show.html', 
    user_id = User.getById({'id' : id}))


# Deletes user
@app.route('/users/delete/<int:id>')
def delete_user(id):

    User.deleteById({'id' : id})
    return redirect('/users')

# Edit User form
@app.route('/users/<int:id>/edit')
def update_form(id):
    print(id)
    return render_template('edit.html', 
    user_update = User.getById({'id' : id}))


@app.route('/users/update/<int:id>', methods=["POST"])
def edit_user(id):

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : id
    }
    User.editById(data) 
    return redirect('/users')
