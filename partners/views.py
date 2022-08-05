from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PartnerForm, LoginForm, RegisterForm, UpdateForm  # RawPartnerForm
from .models import Partner, Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def partner_create_view(request):
    form = PartnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PartnerForm()
    context = {
        'state': "新增夥伴",
        'form': form
    }
    return render(request, "partners/partner_create.html", context)


def partner_delete_view(request, par_id):
    obj = get_object_or_404(Partner, id=par_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "partners/partner_delete.html", context)


def partner_update_view(request, par_id):
    obj = get_object_or_404(Partner, id=par_id)
    form = PartnerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'state': "更新夥伴",
        'form': form
    }
    return render(request, "partners/partner_create.html", context)


def partner_list_view(request):
    queryset = Partner.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "partners/partner_list.html", context)


def partner_detail_view(request, par_id):
    obj = Partner.objects.get(id=par_id)
    context = {
        'object': obj
    }
    return render(request, "partners/partner_detail.html", context)


# USER相關
def sign_up_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../index/')
    context = {
        'state': "註冊",
        'form': form
    }
    return render(request, 'partners/partner_signup.html', context)


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 內建的登入
            return redirect('../')  # 重新導向到索引頁
        else:
            messages.warning(request, '登入失敗')

    context = {
        'form': form
    }
    return render(request, 'partners/partner_login.html', context)


def index_view(request):
    return render(request, 'partners/partner_index.html')


def information_view(request):
    user = request.user
    form1 = RegisterForm(request.POST or None, instance=user)
    queryset = Account.objects.all()
    messages.warning(request, '注意！您登出前請先妥善存檔')
    context = {
        'form1': form1,
        'user_list': queryset
    }
    return render(request, 'partners/partner_information.html', context)


def update(request):
    user = request.user
    form = UpdateForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('../')
    context = {
        'state': "更新資料",
        "user_list": form
    }
    return render(request, 'partners/partner_update.html', context)


def logout_view(request):
    logout(request)  # 內建的登出
    return redirect('../index')


def delete_user(request):
    request.user.delete()
    return redirect('../index')

