import pathlib
import random

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest

from .alfa_data import Manager

# TODO: Read SITE_URL form env or something else!
SITE_URL = "http://127.0.0.1:8000"  # change this to your url site if you need it!
UPLOAD_SIZE_LIMIT = 1500000
SUFFIX_FORMAT = ".txt"
manager_obj = Manager()
file_sys_op = FileSystemStorage()


def get_uploaded_file(uploaded_file: UploadedFile) -> UploadedFile:
    """Validate Uploaded File"""
    if uploaded_file is None:
        return None

    if (
        uploaded_file.size >= UPLOAD_SIZE_LIMIT
        or pathlib.Path(uploaded_file.name).suffix != SUFFIX_FORMAT
        # TODO: this is insecure, use MIME
    ):
        return None
    return uploaded_file


def handel_upload_file(
    request: HttpRequest,
    uploaded_file: UploadedFile = None,
) -> dict | None:
    """
    Handel And Extract:
    - absolute_url
    - input_str
    - file_path
    OutPut:
        - dict {
            absolute_url: str,
            input_str: str,
            file_path: str,
        }
    """
    if not uploaded_file:
        uploaded_file = get_uploaded_file(request.FILES.get("user_txt_upload"))
    if uploaded_file:
        name = file_sys_op.save(uploaded_file.name, uploaded_file)
        file_path = file_sys_op.path(name)
        absolute_url = file_sys_op.url(name)
        with open(file_path, "r", encoding="utf-8") as f:
            input_str = f.read()
        information = {
            "absolute_url": absolute_url,
            "input_str": input_str,
            "file_path": file_path,
        }
        return information
    return None


def decimal_to_binary(decimal_string):
    """
    Convert the ASCII value to its 8-bit binary representation using
    format() function The '08b' format specifier ensures that
    each binary representation is 8 bits long with leading zeros if necessary
    """
    return "".join([format(ord(char), "08b") for char in decimal_string])


def encode_input_string(my_str: str, random_input_num: int) -> tuple[
    str,
    tuple,
    tuple,
]:
    """Encode Text
    Input:
        - my_str : str
        - random_input_num: int
    output:
        - tuple[binary_output : str, n_number : tuple, z_number : tuple]
    """
    random_number = random.randint(23, 331)
    n_number = "n:", int(len(my_str) * 3)
    z_number = "z:", (int(random_number) * 2) + 2
    dic_all_alfa = manager_obj.set_seed((int(random_number) * 2) + 2)
    offset = random_input_num + random_number
    out_str = [
        int(dic_all_alfa.get(char)) + offset  # Add offset to each key!
        for char in my_str
        if char in dic_all_alfa
    ]
    strings_number = "".join(map(str, out_str))
    binary_output = decimal_to_binary(strings_number)
    output = (
        binary_output,
        n_number,
        z_number,
    )
    return output


def decode_input_string(
    my_str,
    bare_z_number,
    bare_n_number,
    b_number,
) -> str | None:
    """Decode Text
    Input:
        - my_str : str
        - bare_z_number : int
        - bare_n_number : int
        - b_number : int
    output:
        - TODO:
    """
    generated_random_number = int((bare_z_number - 2) / 2)
    dic_all_alfa = manager_obj.set_seed(bare_z_number)
    key_length = len(str(dic_all_alfa.get("a")))
    length_str_p = int(len(my_str)) - (key_length - 1)
    reverse_dict = {v: k for k, v in dic_all_alfa.items()}
    offset = b_number + generated_random_number
    out_str = [
        reverse_dict[
            int(my_str[str_range : str_range + key_length]) - offset
        ]  # iterate into characters and return them to original value
        for str_range in range(0, length_str_p, key_length)
    ]
    if float(len(out_str)) != bare_n_number / 3:
        return None
    return "".join(map(str, out_str))


def binary_to_decimal(binary_string):
    """binary to decimal
    Input:
        - binary_string : str
    Output:
        - str
    """
    chunk_size = 8  # each character is represented by '8' bits
    return "".join(
        [
            chr(int(binary_string[i : i + chunk_size], 2))
            for i in range(0, len(binary_string), chunk_size)
        ]
    )


def decimal_to_binary(decimal_string):
    """
    Input:
        - decimal_string : str
    Output:
        - str
    Convert the ASCII value to its 8-bit binary representation using
    format() function The '08b' format specifier ensures that
    each binary representation is 8 bits long with leading zeros if necessary
    """
    return "".join([format(ord(char), "08b") for char in decimal_string])
