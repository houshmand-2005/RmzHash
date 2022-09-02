import requests
urlpath = 'http://127.0.0.1:8000/api/encode/upload/'
test_file = open("normal_text.txt", "r")
test_response = requests.post(
    urlpath, files={"file_uploaded": test_file}, data={"RANDkey": "0"})
print(test_response)
print(test_response.text)
input("done")
