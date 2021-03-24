from django.urls import path
from .views import WomanList, WomanDetail

urlpatterns =[
    path('<int:pk>/', WomanDetail.as_view(), name = 'woman_detail'),
    path('', WomanList.as_view(), name = 'woman_list'),
]