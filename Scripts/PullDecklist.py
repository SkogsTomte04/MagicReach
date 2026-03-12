import requests,json


data = []
cards = {'R': [],
         'G': [],
         'W' : [],
         'B': [],
         'U': [],
         'N': [],
         'M': []}
with open('Scripts\scryfall\scryfalldataset.json','r', encoding='utf-8') as file:
    data = json.load(file)

def SortCard(card):
    color = card['color_identity']
    if len(color) > 1:
        cards['M'].append(card)
        return
    if len(color) < 1:
        cards['N'].append(card)
        return

    cards[color[0]].append(card)
    
for card in data:
    if card['set'] == 'tla':
        #print(card['name'], card['color_identity'],)
        SortCard(card)



for card in cards['R']:
    print(card['name'])
#print(data[0]['set'])

# header = {
#     'User-Agent': 'MagicReach/1.0',
#     'Accept': '*/*'
# }
# payload = {
#     'identifiers': [
#         {
#             'id': '5e51f727-5a9b-4bc7-83a9-dbcf1c933e15'
#         },
#         {
#             'name': "Aang's Journey"
#         },
#         {
#             'set': 'tla',
#             'collector_number': '1'
#         }

#     ]
# }
# x = requests.get('https://api.scryfall.com/sets/tla', headers=header)
# # x = requests.post('https://api.scryfall.com/cards/collection', headers=header,json=payload)

# data = json.loads(x.text)
# keys = data.keys()
# print(keys)
# for item in data['data']:
#     print(item['name'])
   