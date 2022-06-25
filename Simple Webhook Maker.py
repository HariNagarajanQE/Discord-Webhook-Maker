import json

# see https://leovoel.github.io/embed-visualizer/ to test your webhook. Remember to enable webhook mode.

def get_num(what):
    num = ""
    while isinstance(num, str):
        num = input(what)
        try:
            return int(num)
        except ValueError:
            if num:
                print("Hey, that's not a number.")
            else:
                return 0

def dict_eval(d):
    new_dict = {}
    for key, val in d.items():
        if val:
            if isinstance(val, list):
                new_dict[key] = []
                for item in val:
                    new_dict[key].append(dict_eval(item))

            elif isinstance(val, dict):
                d_dict = {}
                for key1, val1 in val.items():
                    d_dict[key1.replace('"', '\"')] = val1.replace('"', '\"')
            else:
                if isinstance(val, int):
                    new_dict[key.replace('"', '\"')] = val
                else:
                    new_dict[key.replace('"', '\"')] = val.replace('"', '\"')
    return new_dict

webhook = {}
t_webhook = {}
print("None of these fields are required, hit enter to skip them\m")
t_webhook['username'] = input("Bot Username: ")
t_webhook['avatar_url'] = input("Bot Icon URL: ")
t_webhook['content'] = input("Message Content: ")
t_webhook['embeds'] = []
for i in range(get_num("number of embeds (can be zero): ")):
    e_webhook = {}
    e_webhook['title'] = input("Embed Title: ")
    e_webhook['description'] = input("Description: ")
    e_webhook['url'] = input("Title URL: ")
    e_webhook['color'] = get_num("Colour:(decimal) ")
    e_webhook['timestamp'] = input("Timestamp is ISO_8601 format: ")
    e_webhook['footer'] = {}
    e_webhook['thumbnail'] = {}
    e_webhook['image'] = {}
    e_webhook['author'] = {}
    e_webhook['footer']['text'] = input("Footer Text: ")
    e_webhook['footer']['icon_url'] = input("Footer Icon: ")
    e_webhook['thumbnail']['url'] = input("Thumbnail URL: ")
    e_webhook['image']['url'] = input("Image URL: ")
    e_webhook['author']['name'] = input("Author Name: ")
    e_webhook['author']['url'] = input("Author Page URL: ")
    e_webhook['author']['icon_url'] = input("Author Icon URL: ")
    e_webhook['fields'] = []
    for j in range(get_num("number of fields: (can be zero) ")):
        f_webhook = {}
        f_webhook['name'] = input("Name: ")
        f_webhook['value'] = input("Value: ")
        if not f_webhook['name'] or not f_webhook['value']:
            continue
        e_webhook["fields"].append(f_webhook)
    t_webhook['embeds'].append(e_webhook)


webhook = dict_eval(t_webhook)
print("Your webhook. Note this has not been correctly checked for all errors.")
print(json.dumps(webhook))