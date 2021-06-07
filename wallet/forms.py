from django import forms


class SendMoneyForm(forms.Form):
    phone_number = forms.CharField(max_length=13, min_length=13)
    amount = forms.IntegerField(min_value=0, max_value=1000000)

