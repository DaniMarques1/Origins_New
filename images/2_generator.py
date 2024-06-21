import requests
from PIL import Image
import io
import pandas as pd
import os

# Create the cache directory if it doesn't exist
cache_directory = "image_cache"
os.makedirs(cache_directory, exist_ok=True)

# Read the CSV file
df = pd.read_csv("Erc1155_info.csv")

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    image_url = row['Image URL']
    id_value = row['ID']
    file_name = f"{id_value}.png"
    file_path = os.path.join(cache_directory, file_name)

    try:
        if not os.path.exists(file_path):
            # If the image is not in the cache, download and save it
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content)).convert("RGBA")
                image.save(file_path)
                print(f"Image file {file_name} downloaded and cached.")
            else:
                print(f"Failed to download image from {image_url}")
                continue
        else:
            print(f"Image file {file_name} already exists in the cache.")

        # Now, open the image from the newly saved file
        image = Image.open(file_path).convert("RGBA")

        # Create the canvas
        canvas = Image.new('RGBA', (500, 500), (0, 0, 0, 0))

        # Calculate the position for the center-left alignment
        center_left_x = 0
        center_left_y = (canvas.height - image.height) // 2
        position = (center_left_x, center_left_y)

        canvas.paste(image, position, mask=image)

        output_file_path = os.path.join(cache_directory, f"output_{file_name}")
        canvas.save(output_file_path)
        print(f"Output image file {output_file_path} created successfully.")

    except Exception as e:
        print(f"An error occurred while processing {file_name}: {e}")

print("All image files processed successfully.")
