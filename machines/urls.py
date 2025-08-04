from django.urls import path
from .views import RVMListCreateAPIView

urlpatterns = [
    path('rvms/', RVMListCreateAPIView.as_view(), name='rvm-list-create'),
]
