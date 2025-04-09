from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('menu/',views.MenuItemsView.as_view()),
    path('menu/<int:pk>',views.singleMenuItamView.as_view()),
    path('menu/items/', views.MenuItemsView.as_view()),
]