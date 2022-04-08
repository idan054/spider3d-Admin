from flask import Flask
from github import Github, InputGitAuthor
from datetime import datetime

# current date and time
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
file_path = "index.json"
token_prt1 = "ghp_M4wHc747B813CJl7E"
token_prt2 = "mtRoEFJdAUsy42sb4Y5"
g = Github(f"{token_prt1}{token_prt2}")
repo = g.get_repo("idan054/Spider3DFlux")

# file = repo.get_contents(file_path, ref="master")  # Get file from branch
# data = file.decoded_content.decode("utf-8")  # Get raw string data
# data += "LOOOLLLL"  # Modify/Create file

# data = """{
#   "HorizonLayout": [
#     {
#       "layout": "logo",
#       "showMenu": true,
#       "showSearch": true,
#       "showLogo": true,
#       "menuIcon": {
#         "name": "line_horizontal_3_decrease",
#         "fontFamily": "CupertinoIcons"
#       },
#       "image": "https://i.imgur.com/LQWSjzt.png"
#     },
#     {
#       "layout": "bannerImage",
#       "isSlider": true,
#       "autoPlay": true,
#       "showNumber": false,
#       "design": "default",
#       "showBackGround": true,
#       "radius": 8,
#       "items": [
#         {
#           "product": 25056,
#           "image": "https://i.imgur.com/84ySdG3.jpg",
#           "padding": 15.0
#         }
#       ]
#     },
#     {
#       "layout": "bannerImage",
#       "isSlider": true,
#       "autoPlay": true,
#       "showNumber": false,
#       "design": "default",
#       "showBackGround": true,
#       "radius": 8,
#       "items": [
#         {
#           "category": 4783,
#           "image": "https://i.imgur.com/H0bcI9u.jpg",
#           "padding": 15.0
#         },
#         {
#           "category": 2352,
#           "image": "https://i.imgur.com/H7BJGsh.jpg",
#           "padding": 15.0
#         }
#       ]
#     },
#     {
#       "name": "מדפסות מעולות",
#       "category": 2341,
#       "layout": "threeColumn",
#       "isSnapping": true
#     }
#   ],
#   "Setting": {
#     "MainColor": "#961b1e",
#     "ProductListLayout": "list",
#     "StickyHeader": true,
#     "ProductDetail": "halfSizeImageType",
#     "ShowChat": true,
#     "FontFamily": "Heebo"
#   },
#   "TabBar": [
#     {
#       "layout": "home",
#       "icon": "assets/icons/tabs/icon-home.png",
#       "pos": 100,
#       "key": "j3yj4st8gt"
#     },
#     {
#       "layout": "search",
#       "icon": "assets/icons/tabs/icon-search.png",
#       "pos": 200,
#       "key": "bzl41d82nk"
#     },
#     {
#       "layout": "cart",
#       "icon": "assets/icons/tabs/icon-cart2.png",
#       "pos": 300,
#       "key": "vxll1hkaq6"
#     },
#     {
#       "layout": "profile",
#       "icon": "assets/icons/tabs/icon-user.png",
#       "showChat": true,
#       "pos": 400,
#       "settings": [
#         "order",
#         "wishlist",
#         "darkTheme",
#         "rating",
#         "about"
#       ],
#       "background": "https://i.imgur.com/u2GRG8B.jpeg",
#       "key": "mt0v8wv5c5"
#     },
#     {
#       "layout": "wishlist",
#       "icon": "assets/icons/tabs/icon-heartthin.png",
#       "fontFamily": null,
#       "showChat": false,
#       "pos": 550
#     }
#   ],
#   "Drawer": {
#     "logo": null,
#     "items": [
#       {
#         "type": "home",
#         "show": false
#       },
#       {
#         "type": "blog",
#         "show": true
#       },
#       {
#         "type": "login",
#         "show": true
#       },
#       {
#         "show": true,
#         "type": "category"
#       }
#     ]
#   },
#   "VerticalLayout": {
#     "key": "l7x7ddwj5q",
#     "layout": "menu",
#     "name": "המומלצים שלנו",
#     "isVertical": true
#   },
#   "Version": 1,
#   "Datetime": "15:24:04 - Mon 12 Jul"
# }"""  # Modify/Create file

def pushToGithub(path, message, content, branch):
    author = InputGitAuthor(
        "idan054",
        "idanbit80@gmail.com"
    )
    # source = repo.get_branch("master")
    # repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master

    # if update:  # If file already exists, update it
    try:  # If file already exists, update it
        contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
        # print(f'contents.decoded_content {contents.decoded_content}')
        repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch
        return "File has been updated!"
    except:  # If file doesn't exist, create it
        repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch
        return "File has been added!"

# push(file_path, f"Latest update on {now} (by .py)", data, "main")

# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     # resp = push(file_path, f"Latest update on {now} (by .py)", data, "main")
#     return resp
# if __name__ == '__main__':
#     app.run()
