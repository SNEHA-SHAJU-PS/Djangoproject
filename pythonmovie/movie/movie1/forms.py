from django import forms
from movie.models import Movie
class Movieform(forms.ModelForm):

    class Meta:#inner class

        model=Movie
        fields="__all__"