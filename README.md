# RmzHash

<img src="https://github.com/houshmand-2005/RmzHash/blob/cc5e0adf9256dc55936a6d23e8ad5c23a3b1a6d9/images/RMZhash.jpg" alt="RMZhash" width="1000">

A small funny project :) you can use it online from here : [https://rmzhash.pythonanywhere.com/](https://rmzhash.pythonanywhere.com/)

this app can encode you text to a **encrypted** text so no one can find out what you type then you can decode it to normall text
but just you can decode it becase this app gives some **number and keys** to you and if somone doesn't have it they can't decode your text

like : 
<img src="https://github.com/houshmand-2005/RmzHash/blob/1ceca9d64a2ea57571d8051034fb7a585c0b5ea7/images/howitworks.jpg" alt="howitworks" width="1000">

# How to run
```bash
cd RmzHash
pip install -r requirements.txt
```
# Or use docker
```bash
cd RmzHash
docker build -t RmzHashimage .
docker run -d RmzHashimage
```

**This part is optional!**<br>

if you want set the keys by your self you can do this:<br>
for set the keys(**Your text is encrypted with these keys**) you can set keys automatically by the **randomazer_hash.py** this script gives you a random key for each parameter
like this : 

<img src="https://github.com/houshmand-2005/RmzHash/blob/cc5e0adf9256dc55936a6d23e8ad5c23a3b1a6d9/images/randomazer_hash.jpg" alt="randomazer_hash" width="1000">
 
now replace this dic to RmzHash/EDapp/alfa_data.py dic. now it works but if you have problem contact to me

then 
```bash
python ./manage.py runserver
```

<hr>
you can use upload file or type your text also use the API for useing API with python you can see test_api folder

as you can see the test_api folder the API needs these inputs:
* for encode API
  - file in .txt foramt and less than 1.5 MB
  - a random key to change the keys(optional) if you dont want it enter 0

python code for this: 

```bash
test_response = requests.post(
    urlpath, files={"file_uploaded": test_file}, data={"RANDkey": "0"})
    
print(test_response.text) # the url of encode it file random key the n number and the z number
```

then this API gievs to you some number with this number you can decode it so save them and the encoded file so you must save the file in .txt format.

* for decode API
  - file in .txt foramt and less than 1.5 MB
  - random key if you pass 0 when you encode it here just pass 0 too
  - the n number(when you encode the text this number sent to you)
  - the z number(when you encode the text this number sent to you)

python code for this: 

```bash
test_response = requests.post(urlpath, files={"file_uploaded": test_file}, data={
                              "RANDkey": "0", "nNum": "138", "zNum": "354"})

print(test_response.text) # url of encode it file
```

user uploads files save in RmzHash/textfiles/<br>
## ⭐What's new:
- Now the keys made random and you dont need to do it yourself

if you want change a part of code you can use a pull request.

**This project is just a test and don't enter important information.**
