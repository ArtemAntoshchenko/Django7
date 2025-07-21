from django import forms

class FeedbackForm(forms.Form):
    check=forms.BooleanField(
    label='CheckBox', required=False)

    