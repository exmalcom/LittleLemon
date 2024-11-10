from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define URL route for index() view
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
