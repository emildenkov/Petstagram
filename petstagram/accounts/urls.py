from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>', include([
        path('', views.details_profile_page, name='details-profile'),
        path('edit/', views.edit_profile_page, name='edit-profile'),
        path('delete/', views.delete_profile_page, name='delete-profile'),
    ]))
]