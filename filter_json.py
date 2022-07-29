import json

names = []
with open('naenae.txt', 'r') as f:
    restaurant_data = json.load(f)['data'][0]['gridItems']
    for rdata in restaurant_data:
        names.append(rdata['displayTitle'])
        
with open('restaurant_week.txt', 'w') as f:
    for name in names:
        f.write(name + '\n')
