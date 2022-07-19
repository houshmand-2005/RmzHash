from django.shortcuts import render
from .test_alfa import Dic_All_Alfa, has_duplicates_rand
import os
import random as random
from django.views import View
# Create your views here.


"""
How use Dic_All_Alfa : 
def Dic_All_Alfa(runtest, prammter, needAll, doRand, getRandNUM):
    (has dup for orginal list,
    give you one of the value by the key,
    give you all of the keys,
    randomaze vlaue(dont use for each user this is global),
    create a new random number)
"""


def homepage(request):
    return render(request, 'EDapp/homepage.html')


class EnCoder(View):
    def post(self, request):
        try:    
            show_code = False
            randnum = random.randint(23, 331)
            if request.POST.get('textarea') == "":
                return render(request, 'EDapp/Encode.html')
            bnnum = 0
            cnum = 0
            my_str = request.POST.get('textarea')
            my_str = str(my_str)
            out_str = ([''] * len(my_str)) + ['1']
            num = 0
            # if request.POST.get('RANDkey') != "" & int(request.POST.get('RANDkey')) < 10:
            #     if int(request.POST.get('RANDkey')) > 0:
            #         bnnum = int(request.POST.get('RANDkey')) 
            # else:
            #     bnnum = 0 
            if request.POST.get('RANDkey') != "":
                if int(request.POST.get('RANDkey')) < 11:
                    if int(request.POST.get('RANDkey')) > 0:
                        bnnum = int(request.POST.get('RANDkey')) # i KNOW THAT IT IS BAD CODE, BUT I DONT HAVE TIME TO FIX IT :)
            if request.POST.get('RANDkey') == "":
                bnnum = 0
            if has_duplicates_rand(randnum,bnnum) == True:
                print("I found a *has_duplicates_rand*")
                randnum = random.randint(23, 331)
            for i in range(len(my_str)):
                for alfa in Dic_All_Alfa("False", "", "True","", ""):
                    if my_str[i] == f"{alfa}":
                        out_str[num] = Dic_All_Alfa("False", f"{alfa}", "False", "","") + bnnum + randnum
                        num = num + 1
                        break
            listToStr = ''.join([str(asd) for asd in out_str])
            # THIS IS A BAD PROGRAM ? SO DONT USE IT LOL :) NO REALLY THIS IS JUST FOR TEST AND FOR FUN
            nNUMber = "n:", int((len(my_str) * 3) + cnum)
            zNUMber = "z:", (int(randnum) * 2) + 2
            bin_itemf = format(int(listToStr), "b")
            if bnnum != 0:
                show_code = True
            context = {"the_string": bin_itemf, "nNUM": nNUMber,"zNUM": zNUMber, "bnnum" : bnnum, "show_code" : show_code}
            return render(request, 'EDapp/outPutE.html',context)
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
            # if request.POST.get('RANDkey') != "" & int(request.POST.get('RANDkey')) < 10:
            #     if int(request.POST.get('RANDkey')) > 0:
            #         bnnum = int(request.POST.get('RANDkey')) 
            # else:
            #     bnnum = 0
            bnnum = 0  
            if request.POST.get('RANDkey') != "":
                if int(request.POST.get('RANDkey')) < 10:
                    if int(request.POST.get('RANDkey')) > 0:
                        bnnum = int(request.POST.get('RANDkey')) # i KNOW THAT IT IS BAD CODE, BUT I DONT HAVE TIME TO FIX IT :)
            if request.POST.get('RANDkey') == "":
                bnnum = 0
            cnum = 0
            n = 0
            strbin = int(request.POST.get('textarea'), 2)
            my_str = str(strbin)
            n = int(request.POST.get('nNum'))
            n = int((n - cnum) / 3)
            out_str = [''] * n
            rand_num1 = int(request.POST.get('zNum'))
            rand_num1 = int((rand_num1 - 2) / 2)
            kys = Dic_All_Alfa("", "", "True", "", "")
            for i in range(len(my_str)):
                for alfa_2 in Dic_All_Alfa("", "", "True", "", ""):
                    if int(my_str[fd:fd + 11]) == kys[f"{alfa_2}"] + bnnum + rand_num1:
                        out_str[num] = f"{alfa_2}"
                        num = num + 1
                        fd = fd + 11
            lslfjldf = ''.join([str(aspd) for aspd in out_str])
            context = {"text": lslfjldf}
            return render(request, 'EDapp/outPutD.html',context)
        except:
            return render(request, 'EDapp/Decoder.html')
    if request.method == 'GET':
        return render(request, 'EDapp/Decoder.html')


def Warn(request):
    return render(request, 'EDapp/Warn.html')