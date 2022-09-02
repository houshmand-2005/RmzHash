import requests
urlpath = 'http://127.0.0.1:8000/api/decode/upload/'
test_file = open("encode_text.txt", "r")
test_response = requests.post(urlpath, files={"file_uploaded": test_file}, data={
                              "RANDkey": "0", "nNum": "138", "zNum": "354"})
print(test_response)
print(test_response.text)
input("done")
