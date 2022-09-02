from django.shortcuts import render
from django.views import View
from django.core.files.storage import FileSystemStorage
import random as random
import pathlib
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer, DecodeSerializer
from .alfa_data import manager
from .apifunc import encoder_api, decoder_api

site_url = "http://127.0.0.1:8000/"  # change this to your url site if you need it!

mang_command = manager()


# Api views
class Apihelp(View):
    def get(self, request):
        return render(request, 'EDapp/apihelp.html')


class EncodeViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("values are : file_uploaded and RANDkey")

    def create(self, request):
        status_give = encoder_api(self, request)
        return Response(status_give)


class DecodeViewSet(ViewSet):
    serializer_class = DecodeSerializer

    def list(self, request):
        return Response("values are : file_uploaded and RANDkey(you random key if you have!) and nNum(the n number) and zNum(the z number)")

    def create(self, request):
        status_give = decoder_api(self, request)
        return Response(status_give)

# Encoder and Decoder views


class EnCoder(View):
    def post(self, request):
        try:
            url = ""
            try:
                uploaded_file = request.FILES['user_txt_upload']
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

            if use_upload == False:
                if request.POST.get('textarea') == "":
                    return render(request, 'EDapp/Encode.html')
                my_str = request.POST.get('textarea')
            else:
                with open(url, 'r') as f:
                    my_str = f.read()
            show_code = False
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
                print(
                    "||change your keys if you dont do this you cant Encode or Decode||")
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
            if bnnum != 0:
                show_code = True
            if use_upload:
                with open(url, 'w+') as f:
                    f.write(bin_itemf)
                    pathshow = "your file : " + site_url + relurl
                    context = {"the_string": pathshow, "nNUM": nNUMber,
                               "zNUM": zNUMber, "bnnum": bnnum, "show_code": show_code}
            else:
                context = {"the_string": bin_itemf, "nNUM": nNUMber,
                           "zNUM": zNUMber, "bnnum": bnnum, "show_code": show_code}
            return render(request, 'EDapp/outPutE.html', context)
        except:
            return render(request, 'EDapp/Encode.html')

    def get(self, request):
        return render(request, 'EDapp/Encode.html')


def Decoder(request):
    bnnum = 0
    num = 0
    fd = 0
    if request.method == 'POST':
        try:
            url = ""
            try:
                uploaded_file = request.FILES['user_txt_upload']
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
            if use_upload == False:
                if request.POST.get('textarea') == "":
                    return render(request, 'EDapp/Encode.html')
                strbin = int(request.POST.get('textarea'), 2)
                my_str = str(strbin)
            else:
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
                    pathshow = "your file : " + site_url + relurl
                    context = {"text": pathshow}
            else:
                context = {"text": lslfjldf}
            return render(request, 'EDapp/outPutD.html', context)
        except:
            return render(request, 'EDapp/Decoder.html')
    if request.method == 'GET':
        return render(request, 'EDapp/Decoder.html')


# noraml views
def homepage(request):
    return render(request, 'EDapp/homepage.html')


def Warn(request):
    return render(request, 'EDapp/Warn.html')
