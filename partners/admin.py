from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Brand, Account  # 從.models中引用Product函數建立的模型樣式

admin.site.register(Brand)
admin.site.register(Account)

