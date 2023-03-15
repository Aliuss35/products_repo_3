from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_all_products),
  path('<int:pk>', views.product_by_id)
]