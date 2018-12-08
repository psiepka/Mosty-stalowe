from django import forms


class QuizzForm(forms.Form):
    question = forms.CharField()
    answers = forms.MultipleChoiceField()
    explantaion = forms.CharField()
