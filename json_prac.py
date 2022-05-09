"""
JSON

Python        Json
Dict          object
list, tuple   array
str           string
int           string
float         float

"""


# import json

# language = {
#     "id:0":{
#         "language": "Python19",
#         "weeks": "13"
#     }
#     "id:0":{
#            "language": "Python19",
#         "weeks": "13"
#     }
        
    
# }

# groups = {
#     "id: 1":{
#         "tittle": "Python19",
#         "nickname": "Zmeika PEPPA",
#         "languge": 1

#     }
# }
# obj = {
#     "name": "Umida",
#     "gender": "Female",
#     "email": "Umida@gmail.com",
#     "groups": [1,2]
# }

# with open("obj_info.json", mode='w') as file:
#     json.dump(obj, file, indent=4)


# json_object = json.dumps(obj)


# json_object = json.loads(json_object)

# python_object = json.load(json_object)




# with open("info_object.json", "r") as file:
#     print(json.load(file)["gender"])





import requests

import json

URL = "https://jsonplaceholder.typicode.com/posts"

def get_response(url:str):
    response = requests.get(url)
    return response.text  #response.json()


def load_python_object(response:str):
    return json.loads(response)




response = get_response(URL)
python_obj = load_python_object(response)
# print(python_obj[1]["body"])
# print(response)



# for obj in python_obj:
#     print(obj["userId"])




class Post:

    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)

    def get_info(self):
        return f'{self.title} {self.body}'

obj1 = python_obj[0]
post = Post(obj1)
# print(post.__dict__)
# print(post.title)
print(post.get_info())


