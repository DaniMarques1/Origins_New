import requests
from PIL import Image
import io
import pandas as pd
import os

cache_directory = "image_cache"

os.makedirs(cache_directory, exist_ok=True)

df = pd.read_csv("Erc1155_info.csv")

for index, row in df.iterrows():
    id_value = row['ID']

    # Check if the "ID" starts with "avt_"
    if id_value.startswith("avt_"):
        image_url = row['Image URL']
        file_name = f"{id_value}.png"
        file_path = os.path.join(cache_directory, file_name)

        if not os.path.exists(file_path):
            # If the image is not in the cache, download and save it
            response = requests.get(image_url)
            image = Image.open(io.BytesIO(response.content))
            image.save(file_path)
            print(f"Image file {file_name} downloaded and cached.")
        else:
            # If the image is in the cache, load it from there
            image = Image.open(file_path)
            print(f"Image file {file_name} loaded from cache.")

        # Create the canvas
        canvas = Image.new('RGBA', (200, 250), (0, 0, 0, 0))

        # Calculate the position for the center-left alignment
        center_left_x = 0
        center_left_y = (canvas.height - image.height) // 2
        position = (center_left_x, center_left_y)

        canvas.paste(image, position, mask=image)

        canvas.save(file_name)

print("All image files created successfully.")
