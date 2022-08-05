from django.urls import path
from .views import (
    partner_list_view,
    partner_create_view,
    partner_detail_view,
    partner_update_view,
    partner_delete_view,
    sign_up_view,
    login_view,
    index_view,
    information_view,
    update,
    logout_view,
    delete_user,
)

app_name = 'partners'
urlpatterns = [
    path('index/', index_view, name='partner-index'),
    path('', information_view, name='partner-information'),
    path('signup/', sign_up_view, name='partner-signup'),
    path('login/', login_view, name='partner-login'),
    path('update_user_infor/', update, name='update-user-date'),
    path('logout/', logout_view, name='partner-logout'),
    path('delete_user/', delete_user, name='partner-delete_user'),

    path('list/', partner_list_view, name='partner-list'),
    path('create/', partner_create_view, name='partner-list'),
    path('<int:par_id>/', partner_detail_view, name='partner-detail'),
    path('<int:par_id>/update/', partner_update_view, name='partner-update'),
    path('<int:par_id>/delete/', partner_delete_view, name='partner-delete'),

]

