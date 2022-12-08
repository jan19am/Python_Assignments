from flask_app.models.dojo import Dojo
from flask_app import app
from flask import render_template,redirect,request,session,flash

# All dojos
@app.route('/dojos')
def display_all_dojos():

    return render_template('index.html', 
    all_dojos = Dojo.get_all())

@app.route('/create_dojo', methods=["POST"])
def create_dojos():
    
    Dojo.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def display_dojo(dojo_id):

    return render_template('show.html', 
    dojo = Dojo.get_dojo_with_ninjas({'id' : dojo_id}))
