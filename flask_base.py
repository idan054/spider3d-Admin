from flask import Flask, render_template, request
from main import pushToGithub
from flask import Flask
from github import Github, InputGitAuthor
from datetime import datetime

# current date and time
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
file_path = "index.json"
token_prt1 = "ghp_M4wHc747B813CJl7E"
token_prt2 = "mtRoEFJdAUsy42sb4Y5"
g = Github(f"{token_prt1}{token_prt2}")
# g = Github(login_or_token="idanbit80@gmail.com", password="Biton0542331@")
repo = g.get_repo("idan054/Spider3DFlux")

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["first name"]
        # name = request.form
        resp = pushToGithub(file_path, f"Latest update on {now} (by .py)", name, "main")
        return render_template("resp.html", name=name, resp=resp) # age.html

    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
