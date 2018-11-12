import json

#  Read from the json file
json_path = ".\..\..\data\\json_files\\sampledata.json"
# x = '{ "name" : "john", "age" : 30, "city" : "New York"}'
# y = json.loads(x)
#
# print(y["age"])

# READ from file
with open(json_path , "r") as read_file:
    data = json.load(read_file)

    # print(data["children"][0])
    child = data["children"][0]
    print(child)
    print(child["firstName"])
    print(child["age"])

    # accessing an array in json
    print(data["hobbies"])
    for hob in data["hobbies"]:
        print(hob)
