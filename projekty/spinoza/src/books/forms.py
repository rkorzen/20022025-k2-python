from django import forms
from .models import Genre
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class BasicGenreForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)


class GenreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
    

        self.helper.add_input(Submit('submit', 'Dodaj'))

    class Meta:
        model = Genre
        fields = ["name", "description"]