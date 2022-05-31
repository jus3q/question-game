from django import forms
from django.forms.widgets import NumberInput
from questions.models import Rating

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate4', 'rate6',]

class RangeInput(NumberInput):
    input_type = 'range'

class AdvertisePostForm(forms.ModelForm):
     class Meta:
        model = Rating
        fields = ['duration',]
        # duration = forms.IntegerField(widget=forms.RangeInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '148'}), required=False)
        widgets = {
            'duration' : RangeInput(attrs={'max': 10,
                                            'min':1,
                                            'step':1,
                                            'default':5,}
                                            )
        }