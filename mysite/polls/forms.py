from django import forms


class CreateForm(forms.Form):
    question_name = forms.CharField(label="New question name", max_length=100)