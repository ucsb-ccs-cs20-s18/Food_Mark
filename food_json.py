import json
from pprint import pprint
import random

with open('food.json') as json_data:
    foods = json.load(json_data)
    
print('THE FOLLOWING FOODS CONTAIN VITAMIN B12 GREATER THAN 30')

foodlist = []

for food in foods:
    if food['Data']['Vitamins']['Vitamin B12'] > 30:
        foodlist.append(food['Description'])
        print(food['Description'])

print('HERE IS A RANDOM ONE FOR YOU TO TRY TODAY')

i = random.randint(1,len(foodlist))

print(foodlist[i-1])
