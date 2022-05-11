import re

from django import forms

from userprofile.models import Profile


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, help_text="username")
    nickname = forms.CharField(label='nickname', max_length=50, help_text="nickname")
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
            raise forms.ValidationError('该用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = Profile.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("该邮箱已存在")
        else:
            raise forms.ValidationError("请输入正确的邮箱格式")

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
                raise forms.ValidationError('该账号不存在')
        else:
            filter_result = Profile.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError('该账号不存在')

        return username
