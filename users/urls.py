from django.urls import path

from .views import bulk_create_users

urlpatterns = [
    path('', bulk_create_users, name="bulk-create-users"),
]