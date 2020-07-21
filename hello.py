# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap

# @app.route('/about')
# def about():
#   return render_template("aboutus.html")






from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app


@app.route('/')
def home():
    return "Hello"


@app.route('/hashtags/<name>')
def about(name):
  animal = name
  return render_template("aboutus.html", value=animal)


@app.route("/welcome/<name>") 
def welcome_name(name): 
  return "Welcome " + name + "!" 

if __name__ == '__main__':
  app.run(host='0.0.0.0')



# do something with app...