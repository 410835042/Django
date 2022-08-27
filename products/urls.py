from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_update_view,
    product_list_view
)

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-list'),
    path('<int:p_id>/', product_detail_view, name='product-detail'),
    path('<int:p_id>/update/', product_update_view, name='product-update'),
    path('<int:p_id>/delete/', product_delete_view, name='product-delete'),
    # path('products/<int:p_id>/', dynamic_lookup_view, name='product-detail'),
]

