import json


dane = {"user": "rkorzen", "token": "123123sdf", "text": "zażółć gęślą jaźń"}
dane_j = json.dumps(dane)
print(dane_j, type(dane_j))


t = '{"user": "rkorzen", "token": "123123sdf", "text": "za\u017c\u00f3\u0142\u0107 g\u0119\u015bl\u0105 ja\u017a\u0144"}'


dane2 = json.loads(t)
print(dane2, type(dane2))

print(json.dumps(dane2))

data_b: bytes = b'{"user": "rkorzen", "token": "123123sdf"}'
decoded_data_b =  json.loads(data_b.decode('utf-8'))
print(decoded_data_b)
print(json.dumps(decoded_data_b))

# json_params: dict = request.get_json()
# data_b: bytes = request.get_data()
# data = json.loads(data_b.decode('utf-8'))