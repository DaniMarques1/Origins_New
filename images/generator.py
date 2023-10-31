import requests
from PIL import Image
import io
import pandas as pd

df = pd.read_csv("Erc1155_info.csv")

for index, row in df.iterrows():
    image_url = row['Image URL']
    id_value = row['ID']
    file_name = f"{id_value}.png"

    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    canvas = Image.new('RGBA', (500, 500), (0, 0, 0, 0))

    position = (0, 0)

    canvas.paste(image, position, mask=image)

    canvas.save(file_name)

    print(f"Image file {file_name} created successfully.")

print("All image files created successfully.")
