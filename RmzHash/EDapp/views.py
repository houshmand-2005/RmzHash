from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .api_views import decoder_api, encoder_api
from .core import (
    SITE_URL,
    binary_to_decimal,
    decode_input_string,
    encode_input_string,
    handel_upload_file,
)
from .serializers import DecodeSerializer, UploadSerializer


# Api views
class Apihelp(View):
    """Example Of Api Written In Python"""

    def get(self, request) -> HttpResponse:
        """Get 'ApiHelp' Page"""
        return render(request, "EDapp/apihelp.html")


class EncodeViewSet(ViewSet):
    """Encode Api View"""

    serializer_class = UploadSerializer  # TODO: CHECK THIS i dont know what that is!

    def list(self) -> Response:
        """TODO:CHECK THIS i dont know what that is!"""
        return Response("values are : file_uploaded and RANDkey")

    def create(self, request) -> Response:
        """Create An Encoded String Through 'Api'"""
        status_give = encoder_api(self, request)
        return Response(status_give)


class DecodeViewSet(ViewSet):
    """Decode Api View"""

    serializer_class = DecodeSerializer

    def list(self) -> Response:
        """TODO:CHECK THIS i dont know what that is!"""
        return Response(
            "values are : file_uploaded and RANDkey(you random key if you have!) and nNum(the n number) and zNum(the z number)"
        )

    def create(self, request: HttpRequest) -> Response:
        """Try To Decoded String Through 'Api'"""
        status_give = decoder_api(self, request)
        return Response(status_give)


class EnCoder(View):
    """Encode view"""

    def post(self, request: HttpRequest) -> HttpResponse:
        """Create An Encoded String"""
        uploaded_file = handel_upload_file(request)
        if uploaded_file:
            absolute_url = uploaded_file.get("absolute_url")
            my_str = uploaded_file.get("input_str")
            url = uploaded_file.get("file_path")
        else:
            if text_area := request.POST.get("textarea"):
                my_str = text_area
            else:
                return render(request, "EDapp/Encode.html")
        random_input_num = 0
        if (
            request.POST.get("RANDkey") and 0 < int(request.POST.get("RANDkey")) < 11
        ):  # validate RANDkey is bigger than 0 and smaller than 11
            # TODO: make this validation better
            random_input_num = int(request.POST.get("RANDkey"))
        binary_output, n_number, z_number = encode_input_string(
            my_str, random_input_num
        )
        show_code = bool(random_input_num)
        if uploaded_file:
            with open(url, "w", encoding="utf-8") as f:
                f.write(binary_output)
                final_path = "your file : " + SITE_URL + absolute_url
        context = {
            "the_string": final_path if uploaded_file else binary_output,
            "nNUM": n_number,
            "zNUM": z_number,
            "bnnum": random_input_num,
            "show_code": show_code,
        }
        return render(request, "EDapp/outPutE.html", context)

    def get(self, request: HttpRequest) -> HttpResponse:
        """return Encode.html"""
        return render(request, "EDapp/Encode.html")


class DeCoder(View):
    """DeCoder view"""

    def post(self, request: HttpRequest) -> HttpResponse:
        """Return decoded text"""
        try:
            uploaded_file = handel_upload_file(request)
        except ValueError as ex:
            print(ex)  # TODO Show The Error to User
            return render(request, "EDapp/Decoder.html")
        if uploaded_file:
            absolute_url = uploaded_file.get("absolute_url")
            my_str = binary_to_decimal(uploaded_file.get("input_str"))
            url = uploaded_file.get("file_path")
        else:
            if text_area := request.POST.get("textarea"):
                my_str = binary_to_decimal(text_area)
            else:
                return render(request, "EDapp/Decoder.html")
        b_number = 0
        if (
            request.POST.get("RANDkey") and 0 < int(request.POST.get("RANDkey")) < 11
        ):  # validate RANDkey is bigger than 0 and smaller than 11
            # TODO: make this validation better
            b_number = int(request.POST.get("RANDkey"))
        z_number_input = request.POST.get("zNum")
        n_num_input = request.POST.get("nNum")
        bare_n_number = int(n_num_input) if n_num_input else 0
        bare_z_number = int(z_number_input) if z_number_input else 0
        final_str = decode_input_string(my_str, bare_z_number, bare_n_number, b_number)
        if not final_str:
            print("nNum is wrong!")
            return render(request, "EDapp/Decoder.html")
        if uploaded_file:
            with open(url, "w", encoding="utf-8") as f:
                f.write(final_str)
            final_path = "your file : " + SITE_URL + absolute_url
        context = {"text": final_path if uploaded_file else final_str}
        return render(request, "EDapp/outPutD.html", context)

    def get(self, request: HttpRequest) -> HttpResponse:
        """return Decoder.html"""
        return render(request, "EDapp/Decoder.html")


def homepage(request: HttpRequest) -> HttpResponse:
    """Show The Home Page"""
    return render(request, "EDapp/homepage.html")


def warning_page(request: HttpRequest) -> HttpResponse:
    """Show The Warning Page"""
    return render(request, "EDapp/Warn.html")
