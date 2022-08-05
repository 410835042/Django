from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Partner, Account  # 從.models中引用Product函數建立的模型樣式

admin.site.register(Partner)
admin.site.register(Account)

