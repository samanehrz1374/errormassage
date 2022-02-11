from dataclasses import fields
from django import forms
from .models import erormsg



class profileform(forms.ModelForm):
    name=forms.CharField(max_length=100)
    family=forms.CharField(max_length=100)
    class Meta:
        model=erormsg
        fields=['name','family']

    def clean(self,*args, **kwargs):
        # cleaned_data = super(profileform, self).clean()
        name = self.cleaned_data.get("name")
        family = self.cleaned_data.get("family")

        if name != family:
            raise forms.ValidationError("کاربر")
        return name