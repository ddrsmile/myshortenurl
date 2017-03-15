from django import forms

class SubmitURLForm(forms.Form):
    url = forms.URLField(label='Submit URL',
                         required=False,
                         widget=forms.TextInput(attrs={'placeholder': 'Your Original URL'}))