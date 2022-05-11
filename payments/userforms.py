import re

from django import forms

from payments.models import Profile


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, help_text="username")
    nickname = forms.CharField(label='nickname', max_length=50, help_text="nickname")
    firstname = forms.CharField(label='firstname', max_length=50, help_text="firstname")
    lastname = forms.CharField(label='lastname', max_length=50, help_text="lastname")
    email = forms.EmailField(label='email', help_text="email")
    password = forms.CharField(label='password', help_text="password", widget=forms.PasswordInput)
    tel_number = forms.CharField(label="tel_number", help_text="tel_number")
    gender = forms.CharField(label="gender", help_text="gender")
    type = forms.CharField(label="type", help_text="type")
    # balance = models.DecimalField(verbose_name="金额", max_digits=10, decimal_places=2, blank=True, default=0)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = Profile.objects.filter(username__exact=username)
        if len(filter_result) > 0:
            raise forms.ValidationError('The username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = Profile.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("The email already exists")
        else:
            raise forms.ValidationError("The email format is incorrect")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        return password


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, help_text="username or email")
    password = forms.CharField(label='password', widget=forms.PasswordInput, help_text="password")

    # print(username, password)
    # use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if email_check(username):
            filter_result = Profile.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError('The username is invalid')
        else:
            filter_result = Profile.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError('The usrname is invalid')

        return username


class ContactForm(forms.Form):
    #from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
