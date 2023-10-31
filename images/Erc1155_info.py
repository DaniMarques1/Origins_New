import requests
import json
import pandas as pd
import io

url = "https://api-gateway.skymavis.com/origins/v2/community/items"
headers = {
    "accept": "application/json",
    "X-API-Key": "bm5fVQSFG0HKBEjKcBG2hMJXg4wUwGmr"
}

limit = 100
offset = 0
items = []

while True:
    params = {
        "limit": limit,
        "offset": offset
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)
    batch_items = data["_items"]
    if not batch_items:
        # No more items, exit the loop
        break
    items.extend(batch_items)
    offset += limit

id_list = []
display_order_list = []
category_list = []
rarity_list = []
description_list = []
name_list = []
token_standard_list = []
token_address_list = []
token_id_list = []
image_url_list = []

for item in items:
    id_list.append(item["id"])
    display_order_list.append(item.get("displayOrder"))
    category_list.append(item["category"])
    rarity_list.append(item["rarity"])
    description_list.append(item.get("description"))
    name_list.append(item["name"])
    token_standard_list.append(item["tokenStandard"])
    token_address_list.append(item["tokenAddress"])
    token_id_list.append(item["tokenId"])
    image_url_list.append(item["imageUrl"])

parsed_data = {
    "ID": id_list,
    "Display Order": display_order_list,
    "Category": category_list,
    "Rarity": rarity_list,
    "Description": description_list,
    "Name": name_list,
    "Token Standard": token_standard_list,
    "Token Address": token_address_list,
    "Token ID": token_id_list,
    "Image URL": image_url_list
}

df = pd.DataFrame(parsed_data)
print(df)
df.to_csv("Erc1155_info.csv", index=False)
