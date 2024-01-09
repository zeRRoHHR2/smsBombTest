import requests

check = requests.get("https//:github.com/")
print(check)

phone=input("Введіть номер підара +380")
try:
    requests.post("requests.post('https://my.vodafone.ua/primary/auth?language=ua',data={'phone':phone})")
except:
    print('-')