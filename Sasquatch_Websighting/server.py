from flask_app import app
from flask_app.controllers import users, login_reg_controller, posts


if __name__=="__main__":
    app.run(debug=True)