from django import forms


class YomiForm(forms.Form):
    pinyin = forms.CharField(label='pinyin', max_length=10)
