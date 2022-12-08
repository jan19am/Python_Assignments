from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app
from flask import render_template,redirect,request,session,flash


@app.route('/ninjas')
def display_ninja():

    return render_template('ninja.html', all_dojos = Dojo.get_all())

@app.route('/create_ninja', methods=["POST"])
def create_ninjas():
    
    Ninja.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')
