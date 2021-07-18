# form_resp = {
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

def config_by_resp(form_resp):
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
            # "my_slider_num": form_resp["slider_num"][forIndex],
        })
        forIndex += 1

    # print(items_dict)

    ## Get current online config and edit
    import urllib.request, json
    with urllib.request.urlopen("https://config-fluxstore-idan054.vercel.app/") as url:
        try:
            full_config = json.loads(url.read().decode())
        except:
            full_config = url.read()
        print(type(full_config))
        print(full_config)

    # place final "items" of full config
    forIndex = 0
    for item in full_config["HorizonLayout"]:
        # print(item)
        if item["layout"] == "bannerImage":
            try:
                # print(full_config["HorizonLayout"][forIndex]["items"])
                print(forIndex)
                full_config["HorizonLayout"][forIndex]["items"] = \
                    items_dict[f"{forIndex}"]["items"]
            except:
                pass
        forIndex += 1
    # print(full_config["HorizonLayout"])
    # print(full_config)
    return full_config


