from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comments


class MyMailField(forms.EmailField):
    def __init__(self, **kwargs):
        super(MyMailField, self).__init__(**kwargs)
        self.required = True


class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')
        field_classes = {'email': MyMailField}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'arkasha2000'}),
            'email': forms.EmailInput(attrs={'placeholder': 'arkasha@mail.ru'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Аркадий'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Аркадьев'})
        }

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                     'placeholder': '********'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                     'placeholder': '********'})


class NewCommentForm(forms.Form):
    comment_text = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Здесь можно оставить свой комментарий'
            }
        ),
        label='Комментарий'
    )


class SearchForm(forms.Form):
    search_text = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'найди своё...'
            }
        ),
        label='Поиск'
    )
