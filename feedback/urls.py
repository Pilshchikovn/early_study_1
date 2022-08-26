from django.contrib import admin
from django.urls import path
from . import views
from .views import FeedBackView,DoneView

urlpatterns = [

    path('', FeedBackView.as_view()),
    # path('<int:id_feedback>', views.update_feedback),
    path('done', views.DoneView.as_view()),
    path('list', views.ListFeedbackView.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view()),
    path('update/<int:pk>', views.FeedBackViewUpdate.as_view()),
    # path('detail/<int:id_feedback>', views.DetailFeedBack.as_view()),
    # path('done', views.done),
    # path('', views.index),

]
