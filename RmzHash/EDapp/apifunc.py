from django.core.files.storage import FileSystemStorage
import random as random
import pathlib
from .alfa_data import manager
site_url = "http://127.0.0.1:8000/" # change this to your url site if you need it!

mang_command = manager()


def encoder_api(self, request):
    try:
        url = ""
        try:
            uploaded_file = request.FILES['file_uploaded']
            use_upload = True
        except:
            use_upload = False
        if use_upload:
            if uploaded_file.size < 1500000 and pathlib.Path(uploaded_file.name).suffix == ".txt":
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name, uploaded_file)
                use_upload = True
                url = fs.path(name)
                relurl = fs.url(name)
        with open(url, 'r') as f:
            my_str = f.read()
        randnum = random.randint(23, 331)
        bnnum = 0
        cnum = 0
        my_str = str(my_str)
        out_str = ([''] * len(my_str)) + ['1']
        num = 0
        if request.POST.get('RANDkey') != "" and int(request.POST.get('RANDkey')) < 11 and int(request.POST.get('RANDkey')) > 0:
            bnnum = int(request.POST.get('RANDkey'))
        else:
            bnnum = 0
        if mang_command.has_duplicates_rand(randnum, bnnum) == True:
            print("I found a *has_duplicates_rand*")
            print("|change your keys if you dont do this you cant Encode or Decode|")
            randnum = random.randint(23, 331)
        for i in range(len(my_str)):
            for alfa in mang_command.needAll():
                if my_str[i] == f"{alfa}":
                    out_str[num] = mang_command.giveAprammter(
                        f"{alfa}") + bnnum + randnum
                    num = num + 1
                    break
        listToStr = ''.join([str(asd) for asd in out_str])
        # THIS IS A BAD PROGRAM ? SO DONT USE IT LOL :) NO REALLY THIS IS JUST FOR TEST AND FOR FUN
        nNUMber = "n:", int((len(my_str) * 3) + cnum)
        zNUMber = "z:", (int(randnum) * 2) + 2
        bin_itemf = format(int(listToStr), "b")
        if use_upload:
            with open(url, 'w+') as f:
                f.write(bin_itemf)
                pathshow = site_url + relurl
                returnval = pathshow, nNUMber, zNUMber, bnnum
                return returnval
    except:
        print("problem")


def decoder_api(self, request):
    bnnum = 0
    num = 0
    fd = 0
    try:
        url = ""
        try:
            uploaded_file = request.FILES['file_uploaded']
            use_upload = True
        except:
            use_upload = False
        if use_upload:
            if uploaded_file.size < 1500000 and pathlib.Path(uploaded_file.name).suffix == ".txt":
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name, uploaded_file)
                use_upload = True
                url = fs.path(name)
                relurl = fs.url(name)
        with open(url, 'r') as f:
            my_strpre = f.read()
        strbin = int(my_strpre, 2)
        my_str = str(strbin)
        bnnum = 0
        if request.POST.get('RANDkey') != "" and int(request.POST.get('RANDkey')) < 10 and int(request.POST.get('RANDkey')) > 0:
            bnnum = int(request.POST.get('RANDkey'))
        elif request.POST.get('RANDkey') == "":
            bnnum = 0
        cnum = 0
        n = 0
        n = int(request.POST.get('nNum'))
        n = int((n - cnum) / 3)
        out_str = [''] * n
        rand_num1 = int(request.POST.get('zNum'))
        rand_num1 = int((rand_num1 - 2) / 2)
        kys = mang_command.needAll()
        for i in range(len(my_str)):
            for alfa_2 in mang_command.needAll():
                if int(my_str[fd:fd + 11]) == kys[f"{alfa_2}"] + bnnum + rand_num1:
                    out_str[num] = f"{alfa_2}"
                    num = num + 1
                    fd = fd + 11  # or use len() for get size of the key
        lslfjldf = ''.join([str(aspd) for aspd in out_str])
        if use_upload:
            with open(url, 'w+') as f:
                f.write(lslfjldf)
                pathshow = site_url + relurl
                return pathshow
    except:
        print("problem")
