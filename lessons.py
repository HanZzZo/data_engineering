# YAML
#import yaml

#write
# l_connections = [
#     {
#         "user_name": "etl_user",
#         "password": "123"
#     },
#     {
#         "user_name": "test_user",
#         "password": "456"
#     }
# ]

# with open(r'C:\Users\ddenisenkov\Documents\Обучение\data_engineering\fruits.yaml', 'w') as file:
#     documents = yaml.dump(l_connections, file)

# #reading
# with open(r'fruits.yaml') as file:
#    connections= yaml.load(file, Loader=yaml.FullLoader)
   
#    print(connections)
#    print(type(connections))


#JSON
# import json

# dictionsry = {
#     "name": "sath",
#     "rol": "lcks",
#     "dfvljk": 45678
# }

# json_object = json.dumps(dictionsry, indent=4)

# #writ
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
    
# with open('sample.json', 'r') as openfile:    
#     json_object = json.load(openfile)
    
# print(json_object)


#CSV
import pandas as pd

l_connections = [
    {
        "user_name": "etl_user",
        "password": "123"
    },
    {
        "user_name": "test_user",
        "password": "456"
    }
]

df1 = pd.DataFrame(l_connections )
#print(df1)

df1.to_csv("from_pandas.csv")

df2 = pd.read_csv("from_pandas.csv")
print(df2)