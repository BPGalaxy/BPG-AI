from django import forms

class UserRegisterForm(forms.Form):
    Username = forms.CharField(label="Username", required=False, widget=forms.TextInput(attrs={"required":True}))
    Email = forms.EmailField(label="Email", required=False, widget=forms.TextInput(attrs={"required":True}))
    Password = forms.CharField(label="Password", required=False, widget=forms.PasswordInput(attrs={"required":True}))

class UserLoginForm(forms.Form):
    Username = forms.CharField(
        label="Username",
        required=False,
        widget=forms.TextInput(attrs={
            "required": True,
            "placeholder": "Enter your username",
            "class": "form-input"
        })
    )
    Password = forms.CharField(
        label="Password",
        required=False,
        widget=forms.PasswordInput(attrs={
            "required": True,
            "placeholder": "Enter your password",
            "class": "form-input"
        })
    )