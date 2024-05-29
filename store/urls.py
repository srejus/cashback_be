from django.urls import path
from  .views import *

urlpatterns = [
    path('',ListStoreApi.as_view()),
    path('<int:id>/',ListStoreApi.as_view()),
]