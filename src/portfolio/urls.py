from django.urls import path
from .views import ModuleFeedView

urlpatterns = [
    path('', ModuleFeedView.as_view(), name='portfolio-index'),
]
