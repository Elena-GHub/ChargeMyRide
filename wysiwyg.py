import json


with open('data/charging_stations.json') as data:
    json_return = json.load(data)
    print(json_return['data'][0]['latitude'])
    
    # for key, value in json_return.data():
    #     print(key,':',value)

    # for key in json_return:
    #     for item in 
    #     print(key, ':', json_return[key])
