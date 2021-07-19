from django import forms
from django.forms.widgets import RadioSelect
from django.forms import ModelForm

# Create the form class.
     
true_false = [(True, 'True'), (False, 'False')]

class BoolForm(forms.Form):
    user_choice = forms.ChoiceField(label = '' , choices=true_false, widget=RadioSelect)
    
class QuizForm(forms.Form):
    quiz = forms.CharField(label='')
    answer = forms.ChoiceField(label = '' , choices=true_false, widget=RadioSelect)