import json

# convert a dictionary to a json file
dir_path = os.path.dirname(os.path.realpath(__file__))
my_family = { 
    'parents':['Beth', 'Jerry'],
      'children': ['Summer', 'Morty']
 }
#convert to a json file 
# dump and dumps
with open(f'{dir_path}\\family.json','w', encoding = 'utf-8') as f:
     json.dump(my_family, f)

# convert a dict in json file string
json_family = json.dumps

# load()and loads

with open(f'{dir_path}\\family.json','r', encoding = 'utf-8') as f:
     my_family2 = json.load(f)