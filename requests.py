import requests
import json

pet_1 = 'Бумер'
pet_2 = 'Прайд'

data = {
  'id': 0,
  'category': {'id': 0, 'name': 'string'},
  'name': pet_1,
  'photoUrls': ['string'],
  'tags': [{'id': 0, 'name': 'string'}],
  'status': 'available'
}

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Host': 'petstore.swagger.io',
    'Content-Length': '236',
    'Cache-Control': 'no-cache'
}

# POST-запрос
res_1 = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(data))

print(res_1.status_code)
print(f'\nСоздан питомце "{pet_1}"\nКод ответа - 200\n')

pet_id = dict(res_1.json())['id']

data['id'] = pet_id
data['name'] = pet_2

# PUT-запрос
res_2 = requests.put(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(data))

print(res_2.status_code)
print(f'\nИмя питомца "{pet_1}" изменено на "{pet_2}"\nКод ответа - 200')

print('\nЗапрос данных о питомце с сервера по id - ' + str(pet_id))

# GET-запрос
res_3 = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_3.status_code)
print(f'\nНа сервере имеются данные о питомце\nКод ответа - 200 ')

print('\nУдаление данных о питомце с сервера по id - ' + str(pet_id))

# DELETE-запрос
res_4 = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_4.status_code)
print(f'\nС сервера удалены данные о питомце\nКод ответа - 200')

print('\nПовторный запрос данных о питомце с сервера по id - ' + str(pet_id))

# Повторный GET-запрос
res_5 = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_5.status_code)
print('\nНа сервере нет данных о питомце\nКод ответа - 404')
