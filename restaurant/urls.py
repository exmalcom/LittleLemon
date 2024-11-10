from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),  # Define URL route for index() view
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
]
