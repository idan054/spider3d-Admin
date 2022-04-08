# flask_formDesign.py
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from configByResp import config_by_resp
from main import pushToGithub
from flask import Flask
from github import Github, InputGitAuthor
from datetime import datetime
from flask import jsonify


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
            form_resp = request.form.to_dict(flat=False)
            print(form_resp)
            final_config = config_by_resp(form_resp=form_resp, live_config=True)
            name = request.form["pic_link"]
            # name = final_config
            resp = pushToGithub(file_path, f"Latest update on {now} (by .py)",
                                str(final_config), "main")

            return render_template("resp.html", name=name, resp=resp) # age.html


    import urllib.request, json
    url = urllib.request.urlopen("https://config-fluxstore-idan054.vercel.app/")
    full_config = json.loads(url.read().decode())

    sliderData = []
    full_config['bannerImage_UpdatedAt'] = f'{now}'
    print(full_config["bannerImage_UpdatedAt"])

    i = 0
    for item in full_config["HorizonLayout"][1]['items']:
        dictSample = {'category': '5707', 'image': 'https://www.spider3d.co.il/wp-content/uploads/2022/04/Anycubic-129.jpg', 'padding': 15.0}
        dictKeys = list(item)
        dictValues = list(item.values())
        # print(dictKeys[i])
        # print(dictValues[i])
        # print(f'{dictKeys[i]}: {dictValues[i]}')
        # sliderData.append(f'{dictKeys[i]}: {dictValues[i]}')

        # iKey = 0
        # for key in dictKeys:
        #     if key == 'padding': pass
        #     else:
        #         print(f'{dictKeys[iKey]}: {dictValues[iKey]}')
        #         sliderData.append(f'{dictKeys[iKey]}: {dictValues[iKey]}\n')
        #     iKey += 1

        # print(f'\n{item}'.replace(", 'padding': 15.0}", "").replace('{', ""))
        sliderData.append(f'\n{item}'.replace(", 'padding': 15.0}", "").replace('{', ""))
        print()
        i += 1
    print(f'{sliderData}'.replace(',', ''))


        # dictSample.
        # print(item)
        # print(item.value)

    itemA = ''
    itemB = ''
    itemC = ''
    itemD = ''

    for item in sliderData:
        if itemA == '': itemA = item
        elif itemB == '': itemB = item
        elif itemC == '': itemC = item
        elif itemD == '': itemD = item

    return render_template("form_design/index.html",
                           itemA=f'{itemA}',
                           itemB=f'{itemB}',
                           itemC=f'{itemC}',
                           itemD=f'{itemD}',
                           )


if __name__ == '__main__':
    app.run(debug=True)
