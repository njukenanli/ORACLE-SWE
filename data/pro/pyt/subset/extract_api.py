import json

#with open("data/pro/pyt/5_test_loc_context_api.jsonl") as f:
with open("data/pro/go/5_test_loc_context_api.jsonl") as f:
#with open("data/verified/6_test_loc_context_api.jsonl") as f:
#with open("data/live/5_test_loc_context_api.jsonl") as f:
    l = [json.loads(i) for i in f]

valid_context = [i for i in l if i["error_context"]]
print(len(l), len(valid_context))

res = []

for i in valid_context:
    api_info =  i["api"]
    valid = 0
    al = 0
    for file_path in api_info:
        for func in api_info[file_path]:
            al += 1
            if "file of api definition" in func.keys() and "This API Function needs to be" not in func["api function definition"] and func["api function definition"].strip():
                valid += 1
    if al >= 2 and valid/al >= 0.35:
    #if valid ==8 and al==8:
        print(valid, al, i["instance_id"])
    if i["instance_id"] == "instance_flipt-io__flipt-756f00f79ba8abf9fe53f3c6c818123b42eb7355":
        res = i



with open("data/pro/go/subset/example.json", "w") as f:
    json.dump(res,f, indent="\t")