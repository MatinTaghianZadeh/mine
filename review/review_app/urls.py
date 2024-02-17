from django.urls import path
from review_app import views
urlpatterns = [
    path("", views.index, name="index"),
]