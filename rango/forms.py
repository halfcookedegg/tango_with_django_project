from django import forms
from rango.models import Page, Category
from rango.models import UserProfile
from django.contrib.auth.models import User

MAX_LENGTH_CATEGORY_NAME = 128
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    name = forms.CharField(max_length=Category.name.max_length, help_text="Please enter the category name.")


class Meta:

  model = Category
  fields = ('name',)

class PageForm(forms.ModelForm):
 title = forms.CharField(max_length=128,
 help_text="Please enter the title of the page.")
 url = forms.URLField(max_length=200,
 help_text="Please enter the URL of the page.")
 views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

 class Meta:

  model = Page
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
      model = User
      fields = ('username', 'email', 'password',)
class UserProfileForm(forms.ModelForm):
  class Meta:
     model = UserProfile
     fields = ('website', 'picture',)

exclude = ('category',)

