from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name', 'description', 'author', 'ISBN', 'image']
