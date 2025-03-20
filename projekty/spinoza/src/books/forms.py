from django import forms
from .models import Genre, Author, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm



class BasicGenreForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)



class BooksGenericForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Dodaj'))

class GenreForm(BooksGenericForm):

    class Meta:
        model = Genre
        fields = ["name", "description"]


class AuthorForm(BooksGenericForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    date_of_death = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    class Meta:
        model = Author
        fields = "__all__"


class BookForm(BooksGenericForm):
    class Meta:
        model = Book
        fields = "__all__"


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

