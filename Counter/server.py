from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'clicked' in session:
        print(session['clicked'])
        session['clicked'] += 1
    else:
        session['clicked'] = 1
    return render_template("index.html")

@app.route('/counter', methods = ['post'])
def redirecting():
    print(request.form)
    if request.form['clicked'] == 'Reset':
        session.clear()
    return redirect('/')

@app.route('/', defaults = {'path' : ''})
@app.route('/<path:path>')
def catch_all(path):
    return ('Invalid URL')

if __name__=="__main__":
    app.run(debug=True)