from django.urls import path
from .views import home_page, product_detail

urlpatterns = [
    path('', home_page, name='home'),
    path('<int:id>/', product_detail, name='detail')
]