from rest_framework.serializers import Serializer, FileField, CharField

# Serializers define the API representation.


class UploadSerializer(Serializer):
    file_uploaded = FileField()
    RANDkey = CharField()

    class Meta:
        fields = ['file_uploaded', 'RANDkey']


class DecodeSerializer(Serializer):
    file_uploaded = FileField()
    RANDkey = CharField()
    nNum = CharField()
    zNum = CharField()

    class Meta:
        fields = ['file_uploaded', 'RANDkey', 'nNum', 'zNum']
