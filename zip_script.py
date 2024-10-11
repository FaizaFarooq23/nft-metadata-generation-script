

# Create a zip file with all the metadata and images

import zipfile
import os

# Create a zip file
with zipfile.ZipFile("roburna_autumn_nft.zip", "w") as file:
  # Add all the metadata files
  for i in range(1, 201):
    file.write(f"{i}.json")
  # Add all the image files
  for i in range(1, 201):
    file.write(f"{i}.png")