from django.contrib import admin
from django.urls import path
from . import views
from .views import FeedBackView

urlpatterns = [
    # path('', views.index),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', views.update_feedback),
    path('done', views.done),
]
