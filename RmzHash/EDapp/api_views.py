from .core import (
    SITE_URL,
    binary_to_decimal,
    decode_input_string,
    encode_input_string,
    handel_upload_file,
)


def encoder_api(self, request):
    """Encoder Api view"""
    try:
        uploaded_file = request.FILES["file_uploaded"]
    except Exception:
        return 404
    uploaded_file = handel_upload_file(request, uploaded_file)
    if uploaded_file:
        absolute_url = uploaded_file.get("absolute_url")
        my_str = uploaded_file.get("input_str")
        url = uploaded_file.get("file_path")
    else:
        return 404
    random_input_num = 0
    if (
        request.POST.get("RANDkey") and 0 < int(request.POST.get("RANDkey")) < 11
    ):  # validate RANDkey is bigger than 0 and smaller than 11
        # TODO: make this validation better
        random_input_num = int(request.POST.get("RANDkey"))
    binary_output, n_number, z_number = encode_input_string(
        my_str,
        random_input_num,
    )
    with open(url, "w", encoding="utf-8") as f:
        f.write(binary_output)
    file_path = SITE_URL + absolute_url
    context = file_path, n_number, z_number, random_input_num
    return context


def decoder_api(self, request):
    """Decoder Api view"""
    try:
        uploaded_file = request.FILES["file_uploaded"]
    except Exception:
        return 404
    try:
        uploaded_file = handel_upload_file(request, uploaded_file)
    except ValueError as ex:
        print(ex)  # TODO Show The Error to User
        return 404
    if uploaded_file:
        absolute_url = uploaded_file.get("absolute_url")
        my_str = binary_to_decimal(uploaded_file.get("input_str"))
        url = uploaded_file.get("file_path")
    else:
        return 404
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
    final_str = decode_input_string(
        my_str,
        bare_z_number,
        bare_n_number,
        b_number,
    )
    if not final_str:
        return "nNum is wrong!"
    with open(url, "w", encoding="utf-8") as f:
        f.write(final_str)
    final_path = "your file : " + SITE_URL + absolute_url
    return final_path
