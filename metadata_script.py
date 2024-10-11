
# Create a json file with metadata for the dataset
import json

i = 0

metadata = {
  "name": "Roburna Autumn NFT 2024",
  "description": "The Autumn Collection is a limited release of 200 exclusive NFTs on the Roburna Blockchain.",
}

for i in range(1, 201):
  with open(f"{i}.json", "w") as file:
    metadata["image"] = f"https://ipfs.arbornft.io/roburna_autumn_nft/{i}.png"
    json.dump(metadata, file)