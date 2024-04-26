from django import forms


class ImageDownload(forms.Form):
    image = forms.ImageField()