from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.


def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, p_id):
    obj = get_object_or_404(Product, id=p_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request, p_id):
    obj = Product.objects.get(id=p_id)
    context ={
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_update_view(request, p_id):
    obj = get_object_or_404(Product, id=p_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


"""
def product_create_view(request):
    my_form = RawProductForm() #初始化form
    if request.method == 'POST':  # 若接收到的指令型態為POST
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)#加**代表請求(argument)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)

def product_create_view(request):
    if request.method == 'POST': #若接收到的指令型態為POST
        my_new_title = request.POST.get('title') #將輸入的值存入新變數my_new_title中
        print(my_new_title) #在終端機中輸出my_new_title
    context = {}
    return render(request, "products/product_create.html", context)
    
def dynamic_lookup_view(request, p_id): #依照產品編號顯示內容
    #obj = Product.objects.get(id= p_id)
    obj = get_object_or_404(Product, id=p_id)
    # try:
    #     obj = Product.objects.get(id=p_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
    

def render_initial_data(request):
    initial_data = {
        'title': "my title"
    }
    obj = Product.objects.get(id=7)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
"""
