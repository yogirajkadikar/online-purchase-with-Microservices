# from flask  import Flask, render_template, redirect, url_for, request


# app = Flask(__name__)

# @app.route('/home')
# @app.route('/')
# def home():
#    return render_template('home.html')

# if __name__ == "__main__":
#     app.run(debug=True)

from shop import app

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')