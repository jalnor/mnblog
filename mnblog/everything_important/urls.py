from django.urls import path

from . import views

app_name = 'everything_important'

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:id>/', views.post_detail, name="post_detail"),

]