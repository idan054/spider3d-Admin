from github import Github, InputGitAuthor
from datetime import datetime

# current date and time
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
file_path = "main.py"
token = "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"
g = Github(token)
repo = g.get_repo("idan054/BranchesTesting")

# file = repo.get_contents(file_path, ref="master")  # Get file from branch
# data = file.decoded_content.decode("utf-8")  # Get raw string data
# data += "LOOOLLLL"  # Modify/Create file

data = "LL2"  # Modify/Create file

def push(path, message, content, branch):
    author = InputGitAuthor(
        "idan054",
        "idanbit80@gmail.com"
    )
    # source = repo.get_branch("master")
    # repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master

    # if update:  # If file already exists, update it
    try:  # If file already exists, update it
        contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
        repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch
        print("File has been updated!")
    except:  # If file doesn't exist, create it
        repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch
        print("File has been added!")

push(file_path, f"Latest update on {now} (by .py)", data, "master")
