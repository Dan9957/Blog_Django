from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="Article"
urlpatterns = [
    path('', views.Articles.as_view(), name='Home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)