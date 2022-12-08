import json
 
with open ('config1.json','r',encoding="utf-8") as file:
    data = json.load(file)
 
data["author"] ="Rena"
data["server"]["port"] = 2024
data["server"]["port2"] = 2025
data["openInBrowser"] = True
data["dist"]["fonts"] = "Montserrat"
data["dist"]["fonts"] = "Pier Sans"
data["version"] = "1.0.1"
 
with open("my_config.json", "w") as file:
    json.dump(data, file)
