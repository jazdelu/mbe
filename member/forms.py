from django import forms
from member.models import Member
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.widgets.PasswordInput,
                                label="Password")

	class Meta:
		model = User
		fields = ('username', 'email','password')

	def clean_username(self):
		existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
		if existing.exists():
			raise forms.ValidationError("This username address is already in use. Please supply a different username.")
		return self.cleaned_data['username']

	def clean_email(self):
		existing = User.objects.filter(email__iexact = self.cleaned_data['email'])
		if existing.exists():
			raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
		return self.cleaned_data['email']

	def clean(self):
		if 'cpassword' in self.cleaned_data and 'password' in self.cleaned_data:
			if self.cleaned_data['cpassword'] != self.cleaned_data['password']:
				raise forms.ValidationError("The two password fields didn't match.")
		return self.cleaned_data

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ('kidsname', 'email1','address')


class AuthenticationForm(forms.Form):
	username = forms.CharField(widget=forms.widgets.TextInput)
	password = forms.CharField(widget=forms.widgets.PasswordInput)

	class Meta:
		fields = ['email', 'password']
