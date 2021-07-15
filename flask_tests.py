from flask import Flask, render_template, request
from main import push
from flask import Flask
from github import Github, InputGitAuthor
from datetime import datetime

# current date and time
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
file_path = "index.json"
token = "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"
g = Github(token)
repo = g.get_repo("idan054/Spider3DFlux")

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["first name"]
        resp = push(file_path, f"Latest update on {now} (by .py)", name, "main")
        return render_template("resp.html", name=name, resp=resp) # age.html

    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
