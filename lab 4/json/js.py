import json
with open("sample-data.json") as json_file:
	data = json.load(json_file)
#print(json.dumps(data, indent = 4))
print("Interface Status")
print("="*80	)
given = ["DN", "Description", "Speed", "MTU"]
space = "{:<47}  {:<15}  {:<10}  {:<6}";
print(space.format(*given))
print("-"*47 + "  " + "-"*15 + "  " + "-"*10 + "  " + "-"*6)
n = data["totalCount"]
for i in data["imdata"]:
	dat = i["l1PhysIf"]["attributes"]
	print(space.format(*(dat["dn"], "" if dat.get("description") == None else dat["description"], dat["speed"], dat["mtu"])))