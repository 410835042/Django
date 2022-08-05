from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)  # 在終端機中輸出提出請求的使用者是誰（不安全）
    # return HttpResponse("<h1>Home Page</h1>") #HTML的寫法。 此寫法較不完善，後面改用下行樣式
    return render(request, "home.html", {})  # 從名為home.html模板中抓取此頁應有樣貌


def member_view(request, *args, **kwargs):
    # 建字典
    my_context = {
        "title": "The Following is your information",
        "my_list": [123, 234, 345, "asd"]
    }
    return render(request, "member.html", my_context)


def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def threed_model_view(request):
    return render(request, "3D_model/3d_js.html")

