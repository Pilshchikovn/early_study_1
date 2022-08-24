from django.contrib import admin
from django.urls import path
from . import views
from .views import FeedBackView,DoneView

urlpatterns = [
    # path('', views.index),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', views.update_feedback),
    path('done', views.DoneView.as_view()),
    # path('done', views.done),
]
