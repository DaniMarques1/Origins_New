import requests
from PIL import Image
import io
import pandas as pd
import concurrent.futures

# Read data from the CSV file using pandas
df = pd.read_csv("Erc1155_info.csv")

def process_image(row):
    image_url = row['Image URL']
    id_value = row['ID']
    file_name = f"{id_value}.png"

    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    canvas = Image.new('RGBA', (500, 500), (0, 0, 0, 0))

    position = (0, 0)

    canvas.paste(image, position, mask=image)

    canvas.save(file_name)
    return file_name

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(process_image, df.itertuples()))

for result in results:
    print(f"Image file {result} created successfully.")

print("All image files created successfully.")
