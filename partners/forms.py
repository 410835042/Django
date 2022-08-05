from django import forms
from .models import Partner, Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PartnerForm(forms.ModelForm):
    # 設定提示字 row顯現為1
    company_name = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "品牌名稱",  "rows": 1}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "描述", "rows": 5}))
    email = forms.EmailField(widget=forms.Textarea(attrs={"placeholder": "連絡信箱", "rows": 1}))
    phone_number = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "聯絡電話", "rows": 1}))

    class Meta:
        model = Partner
        fields = [
            'company_name',
            'description',
            'email',
            'phone_number'
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not (email.endswith("com") or email.endswith("tw")):
            raise forms.ValidationError("This is not a valid email")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入帳號", 'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"placeholder": "請輸入密碼", 'class': 'form-control'})
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入帳號", 'class': 'form-control'})
    )

    last_name = forms.CharField(
        label="名稱",
        widget=forms.TextInput(attrs={"placeholder": "請輸入名稱", 'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"placeholder": "請輸入密碼", 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={"placeholder": "請再次輸入密碼", 'class': 'form-control'})
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={"placeholder": "請輸入電子信箱", 'class': 'form-control'})
    )

    phone_number = forms.CharField(
        label="電話號碼",
        widget=forms.TextInput(attrs={"placeholder": "請輸入電話號碼", 'class': 'form-control'})
    )

    class Meta:
        model = Account
        fields = ('username', 'last_name', 'password1', 'password2', 'email', 'phone_number')


class UpdateForm(forms.ModelForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入帳號", 'class': 'form-control'})
    )

    last_name = forms.CharField(
        label="名稱",
        widget=forms.TextInput(attrs={"placeholder": "請輸入名稱", 'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"placeholder": "請輸入密碼", 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={"placeholder": "請再次輸入密碼", 'class': 'form-control'})
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={"placeholder": "請輸入電子信箱", 'class': 'form-control'})
    )

    phone_number = forms.CharField(
        label="電話號碼",
        widget=forms.TextInput(attrs={"placeholder": "請輸入電話號碼", 'class': 'form-control'})
    )

    class Meta:
        model = Account
        fields = ('username', 'last_name', 'password1', 'password2', 'email', 'phone_number')


"""
class RawPartnerForm(forms.Form):
    company_name = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Company Name", "rows": 1}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Description", "rows": 5}))
    email = forms.EmailField(widget=forms.Textarea(attrs={"placeholder": "Contact Email", "rows": 1}))
    phone_number = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Phone Number", "rows": 1}))
"""
