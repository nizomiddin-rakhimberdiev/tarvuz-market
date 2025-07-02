from django.urls import path
from .views import (home_page, 
                    product_detail, 
                    add_product_view, 
                    add_category_view, 
                    add_to_cart_view, 
                    view_cart, 
                    remove_from_cart, 
                    profile_view,
                    plus_cart_view,
                    minus_cart_view
                    )

urlpatterns = [
    path('', home_page, name='home'),
    path('<int:id>/', product_detail, name='detail'),
    path('add-product/', add_product_view, name='add_product'),
    path('add-category/', add_category_view, name='add_category'),
    path('add-to-cart/<int:id>/', add_to_cart_view, name='add_to_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('profile/', profile_view, name='profile'),
    path('plus-cart/<int:id>/', plus_cart_view, name='plus_cart'),
    path('minus-cart/<int:id>/', minus_cart_view, name='minus_cart')
]