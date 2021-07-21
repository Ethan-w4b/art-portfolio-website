from flask import Flask, render_template
from flask import url_for
from flask import send_from_directory
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('home'))

# serve Svelte apps
@app.route("/home")
def home():
    return render_template("home-page.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")




# add the following pages: gallery, contact, news(?)



if __name__ == '__main__':
    app.run(debug=True)
