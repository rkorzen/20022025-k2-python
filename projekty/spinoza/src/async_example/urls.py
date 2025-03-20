from django.urls import path

from . import views

urlpatterns = [
    path("sync-fetch-example/", views.sync_fetch_data, name="sync_fetch_data"),
    path("async-fetch-example/", views.async_fetch_data, name="async_fetch_data"),    
]
