import json
 
# line that we will parse
json_string = """ {
  "orderID": 42,
  "customerName": "John Smith",
  "customerPhoneN": "555-1234",
  "orderContents": [
    {
      "productID": 23,
      "productName": "keyboard",
      "quantity": 1
    },
    {
      "productID": 13,
      "productName": "mouse",
      "quantity": 1
    }
  ],
  "orderCompleted": true
} """
 
# deparced line
parsed_string = json.loads(json_string)

print(parsed_string)
print(parsed_string["customerName"])
print(parsed_string["orderCompleted"])