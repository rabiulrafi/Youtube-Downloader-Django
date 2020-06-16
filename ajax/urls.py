from django.urls import path
from .views import *

urlpatterns =[
    path('',AjaxHandlerView.as_view()),
]