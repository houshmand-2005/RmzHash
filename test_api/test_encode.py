import requests

URL_PATH = "http://127.0.0.1:8000/api/encode/upload/"
with open("normal_text.txt", "r", encoding="utf-8") as file:
    test_response = requests.post(
        URL_PATH, files={"file_uploaded": file}, data={"RANDkey": "0"}
    )
print(test_response)
print(test_response.text)
input("done")
