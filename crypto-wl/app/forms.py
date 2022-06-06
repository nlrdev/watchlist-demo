# -*- coding: utf-8 -*-
from django import forms
from .models import CryptoPair


class CryptoForm(forms.Form):
	crypto = forms.CharField(max_length=100)


class CryptoModelForm(forms.ModelForm):
	name = forms.ChoiceField(label="Select a pair",choices=CryptoPair.objects.all().values_list())
	class Meta:
		model = CryptoPair
		fields = ["name"]
