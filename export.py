from PIL import Image
import os

# Load the PNG file
input_file = "greedIslandV2Assets/tileset.png"
img = Image.open(input_file)

# Specify the output directory path
output_dir = "assetsbox"
os.makedirs(output_dir, exist_ok=True)

# Define the tile size (16x16 pixels)
tile_width = 16
tile_height = 16

def is_empty_tile(tile):
    return tile.getextrema() == ((0, 0),) * 4  # Check if all channels are 0 (fully transparent)

# Loop through the image and extract 16x16 tiles
for y in range(0, img.height, tile_height):
    for x in range(0, img.width, tile_width):
        # Crop the tile
        tile = img.crop((x, y, x + tile_width, y + tile_height))
        
        # Check if the tile is empty
        if not is_empty_tile(tile):
            tile_index = (x // tile_width) + (y // tile_height) * (img.width // tile_width)
            output_filename = os.path.join(output_dir, f"tile_{tile_index}.png")
            tile.save(output_filename)

print(f"Non-empty tiles exported to {output_dir} successfully.")