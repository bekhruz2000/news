from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', register, name='register'),
    path('category/<int:category_id>/', NewsByCategories.as_view(), name='get_categories'),
    path('new/<int:pk>/', NewDetail.as_view(), name="new_detail"),
    path('new/create', CreateNew.as_view(), name='createnew')
]