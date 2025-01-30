import requests
website = input("Website: ")
for i in range(0,9999):
    with requests.get(website) as r:
        print(i, r.status_code)
