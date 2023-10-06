from flask import Flask, render_template, redirect

app = Flask(__name__)
# print(__name__)


@app.route("/")  # home route or index page python decorator
def index():
    return render_template('index.html')


@app.route("/favicon.ico")
def favicon():
    return redirect("/static/favicon.ico")


@app.route("/images/<img>")
def images(img):
    return redirect(f"/static/images/{img}")


@app.route("/assets/css/<file>")
def css(file):
    return redirect(f"/static/assets/css/{file}")


@app.route("/assets/js/<file>")
def js(file):
    return redirect(f"/static/assets/js/{file}")


@app.route("/assets/fonts/<file>")
def fonts(file):
    return redirect(f"/static/assets/fonts/{file}")


if __name__ == "__main__":
    app.run(debug=True)
