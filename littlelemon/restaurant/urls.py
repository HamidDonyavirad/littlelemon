from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.index, name='index'),
    path('api/menu/',views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>',views.singleMenuItamView.as_view()),
    path('api-token-auth/',obtain_auth_token),
]