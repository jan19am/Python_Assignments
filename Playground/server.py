from flask import Flask, render_template
app = Flask(__name__)

# First 3 boxes
@app.route('/play')
def boxes():
    return render_template('index.html')

# Name number of boxes
@app.route('/play/<int:x>')
def level2(x):
    return render_template('box.html', times = x)

# Name number of boxes and color
@app.route('/play/<int:x>/<color>')
def level3(x, color):
    return render_template('play.html', 
    times = x, 
    background = color)


if __name__ == "__main__":
    app.run(debug=True)