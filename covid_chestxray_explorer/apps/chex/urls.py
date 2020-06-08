from django.urls import path
from . import views


urlpatterns = [
    path('xrays/', views.ChestXrayImageList.as_view()),
    path('xrays/<int:pk>/', views.ChestXrayImageDetail.as_view()),
]
