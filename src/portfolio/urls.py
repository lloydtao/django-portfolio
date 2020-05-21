from django.urls import path
from .views import ModuleFeedView, PortfolioFeedView

urlpatterns = [
    path('', ModuleFeedView.as_view(), name='portfolio-index'),
    path('portfolio/', PortfolioFeedView.as_view(), name='portfolio-portfolio'),
]
