from django.urls import path

from api_v1 import views


urlpatterns = [
    path('statistics/', views.StatisticsView.as_view(), ),
    path('statistics/<int:pk>', views.StatisticsView.as_view(), ),
    path('filter/', views.PurchaseList.as_view(), ),
]
