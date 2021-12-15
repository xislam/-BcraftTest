from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api_v1 import views


urlpatterns = [
    path('statistics/', views.StatisticsView.as_view(), ),
    path('statistics/<int:pk>/', views.SnippetDetail.as_view(), ),
    path('filter/', views.PurchaseList.as_view(), ),
]
