from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # 設定提示字 row顯現為1
    title = forms.CharField(label="品名", widget=forms.Textarea(attrs={"placeholder": "請輸入品名", "rows": 1}))
    description = forms.CharField(label="描述", widget=forms.Textarea(attrs={"placeholder": "描述","rows": 5}))
    summary = forms.CharField(label="概要", required=False, widget=forms.Textarea(attrs={"placeholder": "概要","rows": 5}))
    price = forms.DecimalField(label="價格", initial=0.0)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'summary',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "asd" in title:
            raise forms.ValidationError("This is not a valid title")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "品名", "rows": 1}))
    description = forms.CharField( widget=forms.Textarea(attrs={"placeholder": "描述", "rows": 5}))
    summary = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "概要", "rows": 5}))
    price = forms.DecimalField(initial=0.0)



