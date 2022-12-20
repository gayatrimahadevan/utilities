import json
data= json.load(open('terraform.tfstate','r'))
myid="id"
for resources in data.get("resources",[]):
    for resource in resources.keys():
        #if(resource=="name"):
        #   print(f"name: {resources['name']}")
        if(resource=="instances" and resources['mode']=="managed"):
            for ids in resources['instances']:
                print(f"name: {resources['name']} ,arn: {ids['attributes']['arn']}")
#                if(ids['id']=="id"):
#                   print(f"id: {ids['id']}")
