
def config_by_resp(form_resp, live_config):
    items_dict = {}
    forIndex = 0
    ## 1 Setup inner dict to place "items" list
    # EXAMPLE: {'1': {'items': []}, '2': {'items': []}}
    for item in form_resp["slider_num"]:  # post_type represent the quantity of rows on control panel
        items_dict.update({
            form_resp["slider_num"][forIndex]: {"items": []},
        })
        forIndex += 1

    ## 2 place "items" on the right slider
    # EXAMPLE: {'1': {'items': [{'category': '12111', 'image': 'www12', 'padding': 15.0, 'my_slider_num': '1'}]}, '2': {'items': [{'category': '23451', 'image': 'www2', 'padding': 15.0, 'my_slider_num': '2'}]}}
    forIndex = 0
    for item in form_resp["slider_num"]:  # post_type represent the quantity of rows on control panel
        items_dict[form_resp["slider_num"][forIndex]] \
            ["items"].append({
            form_resp["pic_type"][forIndex]: form_resp["pic_num"][forIndex],
            "image": form_resp["pic_link"][forIndex],
            "padding": 15.0,
            # "my_slider_num": resp["slider_num"][forIndex],
        })
        forIndex += 1

    # print(items_dict)

    import urllib.request, json
    if live_config:
        with urllib.request.urlopen("https://config-fluxstore-idan054.vercel.app/") as url:
            try:
                full_config = json.loads(url.read().decode())
            except:
                full_config = url.read()
    else:
        with urllib.request.urlopen("https://config-fluxstore-47g7m0odz-idan054.vercel.app/") as url:
            try:
                full_config = json.loads(url.read().decode())
            except:
                full_config = url.read()

    ## place final "items" of full config
    forIndex = 0
    for item in full_config["HorizonLayout"]:
        # print(item)
        if item["layout"] == "bannerImage":
            try:
                full_config["HorizonLayout"][forIndex]["items"] = []
                # print(full_config["HorizonLayout"][forIndex]["items"])
                print(forIndex)
                full_config["HorizonLayout"][forIndex]["items"] = \
                    items_dict[f"{forIndex}"]["items"]
            except:
                pass
        forIndex += 1
    # print(full_config["HorizonLayout"])
    full_config = json.dumps(full_config, indent=1, ensure_ascii=False)
    print(full_config)
    return full_config


## EXAMPLE
# fform_resp = {'pic_type': ['prot'], 'slider_num': [''], 'pic_num': ['s'], 'pic_link': ['l']}
# fform_resp = {
#   'pic_type': [
#     'product',
#     'product',
#     'category'
#   ],
#   'slider_num': [
#     '1',
#     '1',
#     '2'
#   ],
#   'pic_num': [
#     '12333',
#     '324242',
#     '12333'
#   ],
#   'pic_link': [
#     'www11',
#     'www12',
#     'www2'
#   ]
# }
#
# config_by_resp(form_resp=fform_resp, live_config=False)
