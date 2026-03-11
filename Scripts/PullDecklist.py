import requests,json



header = {
    'User-Agent': 'MagicReach/1.0',
    'Accept': '*/*'
}
payload = {
    'identifiers': [
        {
            'id': '5e51f727-5a9b-4bc7-83a9-dbcf1c933e15'
        },
        {
            'name': "Aang's Journey"
        },
        {
            'set': 'tla',
            'collector_number': '1'
        }

    ]
}
# x = requests.get('https://api.scryfall.com/cards/named?fuzzy=aust+com', headers=header)
x = requests.post('https://api.scryfall.com/cards/collection', headers=header,json=payload)

data = json.loads(x.text)
keys = data['data']
for item in data['data']:
    print(item['name'])
   