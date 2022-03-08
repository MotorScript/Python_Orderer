import json

with open("tea_inventory.json", "r") as f:
    tea_inventory = json.load(f)

for tea in tea_inventory:
    tea["ordered_amount"] =0


with open("tea_inventory.json", "w") as f:
    json.dump(tea_inventory, f, indent=2)