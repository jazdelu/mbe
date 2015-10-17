from django import forms
from member.models import Member
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.widget.PasswordInput,
                                label="Password")
	cpassword = forms.CharField(widget=forms.widget.PasswordInput,
                                label="Password (again)")

	class Meta:
		model = User
		fields = ('username', 'email','password','cpassword')

	def clean_username(self):
		existing = User.objects.filter(username__iexact=self.cleaned__data['username'])
		if existing.exist():
			raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
		return self.cleaned_data['email']

	def clean_email(self):
		if User.objects.filter(email__iexact = self.cleaned_data['email']):
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


class AuthenticationForm(forms.Form):
    """
    Login form
    """
	username = forms.CharField(widget=forms.widgets.TextInput)
	password = forms.CharField(widget=forms.widgets.PasswordInput)

	class Meta:
		fields = ['email', 'password']
