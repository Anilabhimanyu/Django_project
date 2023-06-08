from django import forms
from .models import Course_List

class Course_list_form(forms.ModelForm):
    class Meta:
        model=Course_List
        fields="__all__"