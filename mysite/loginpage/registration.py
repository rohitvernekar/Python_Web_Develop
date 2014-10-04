from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password =forms.CharField(widget=forms.PasswordInput)

    password2=forms.CharField(widget=forms.PasswordInput,label="confirm password")



    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password']

        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2  
