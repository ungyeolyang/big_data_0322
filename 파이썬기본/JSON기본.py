import json

customer = {
     "id": 123456,
    "name" : "KH",
    "history": [
        {"date" : "2023-05-05", "product" : "iPhone 14 Pro"},
        {"date" : "2023-05-10", "product" : "Galuxy S23 Ultra"}
    ]
}

json_string = json.dumps(customer, ensure_ascii=False)
print ((json_string))
