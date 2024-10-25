from django.urls import path, include
from petstagram.photos import views

urlpatterns = [
    path('add/', views.AddPhotoView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailView.as_view(), name='details-photo'),
        path('edit/', views.EditPhotoView.as_view(), name='edit-photo'),
        path('delete/', views.delete_photo, name='delete-photo'),
    ]))
]