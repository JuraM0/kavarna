
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False

    if request.method == "POST":
        message_sent = True

    return render_template(
        "contact.html",
        message_sent=message_sent
    )


if __name__ == "__main__":
    app.run(debug=True)
