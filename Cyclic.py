import urllib, json
url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2&page="
data = []
for i in range(1,6):
    urll = url + str(i)
    response = urllib.urlopen(urll)
    jsondata = json.loads(response.read())
    jlist = jsondata["menus"]
    data = data + jlist


for i in data:
    print i


ids=[]
cid = -1
invalidm = set()
validm = set()
def chckcycle(itemid):
    #for item in data:
    if data[itemid-1]["id"] != cid:
        if data[itemid-1]["child_ids"] == []:
            validm.add(cid)
            return

        for id in data[itemid-1]["child_ids"]:

            chckcycle(id)
    else:
        invalidm.add(cid)
        return


#assuming a cycle is recognized only when the starting node is the ending node
for item in data:
    #print i
    #ids.append(i["id"])
    if item["child_ids"] == []:
        validm.add(item["id"])
    cid = item["id"]

    for id in item["child_ids"]:

        chckcycle(id)

idstoremove = invalidm & validm
validm = {validid for validid in validm if validid not in idstoremove}

print validm
print invalidm


