import urllib, json
from pprint import *

#!!!Assumtions!!!: From the example shown, If a child node of a root node has one cycle all of its child nodes
# are added to the invalid menu with the the root node, even the combinations that does not lead to a cycle
# "children": [5, 18, 3, 6, 1, 20, 7, 19, 4], "root_id": 1} 3 has no cycles but is still added to invalid because it's
#parent node has cycles, simply commenting line 55 will let the program go through every cycle one by one


url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page="
#extra challenge
#url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2&page="
#placing all menus information id dictionary format in a list
def findCycles(url):
    data = []
    for i in range(1,6):
        urll = url + str(i)
        response = urllib.urlopen(urll)
        jsondata = json.loads(response.read())
        jlist = jsondata["menus"]
        data = data + jlist

    return data


data = findCycles(url)
#testing purposes
# for i in data:
#      print i

nodes = {} #holds the root node and all its childeren
childnodes = [] #all the children nodes of a parent node
checklist = [] #used not iterate over nodes that were recursed through

#recurses through all the nodes in id and stores all its childnodes in childnodes
def chckCycleid(id):
    item = data[id-1]

    if item["child_ids"] == []:
        return
    for id in item["child_ids"]:
        if id == cid:
            childnodes.append(id)

            return
        chckCycleid(id)
        childnodes.append(id)


cid = 0 # parent node to compare with childnodes to see if parent node is a cycle
for item in data:
    #going through every node in the url
    cid = item["id"]
    ###comment if the program should not check for a cycle for each node one by one
    if cid not in checklist:
        chckCycleid(cid)
        nodes[cid] = childnodes
        checklist = checklist + childnodes
        childnodes = []

#print nodes

#outputing result to json data
result = {
  "valid_menus": [

  ],
  "invalid_menus": [

  ]
}
nodekeys = list(nodes.keys())

for i in nodekeys:
    if i in nodes[i]:
        values = result["invalid_menus"]
        result["invalid_menus"] = [{"root_id": i,"children": nodes[i]}] + values

    else:
        values = result["valid_menus"]
        result["valid_menus"] = [{"root_id": i,"children": nodes[i]}] + values

output = json.dumps(result)
pprint(result)