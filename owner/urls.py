from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('message/<contact_id>/', views.read_message, name="read_message"),
    path('delete_message/<contact_id>/', views.delete_message,
         name="delete_message"),
    path('mark_unread/<contact_id>/', views.mark_unread,
         name="mark_unread"),
]
