from django import forms
from . models import Projects

class projectForm(forms.ModelForm):
	class Meta:
		model=Projects
		fields=["title","description","image",'link']
		widgets={
		"title":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"title",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Description",
			}),
		"link":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"link",
			}),
		}
