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
# g = Github(login_or_token="idanbit80@gmail.com", password="Biton0542331@")
repo = g.get_repo("idan054/Spider3DFlux")

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # name = request.form["first name"]
        name = request.form
        resp = push(file_path, f"Latest update on {now} (by .py)", name, "main")
        return render_template("resp.html", name=name, resp=resp) # age.html

    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
