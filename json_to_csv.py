import json
import pandas as pd


input_file = "nft_sample.json"
output_csv = "nft_collection.csv"

nft_data = []


with open(input_file, "r") as file:
   
    data = json.load(file)
    for nft in data:
        nft_row = {
            "name": nft.get("name", ""),
            "description": nft.get("description", ""),
            "image": nft.get("image", "")
        }

        attributes = nft.get("attributes", [])
        for attr in attributes:
            trait_type = attr.get("trait_type", "")
            value = attr.get("value", "")
            nft_row[trait_type] = value  

        nft_data.append(nft_row)


df = pd.DataFrame(nft_data)

df.to_csv(output_csv, index=False)


