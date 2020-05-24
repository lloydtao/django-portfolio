from django.urls import path
from .views import ModuleFeedView, PortfolioFeedView, EducationFeedView, SkillsFeedView

urlpatterns = [
    path('', ModuleFeedView.as_view(), name='portfolio-index'),
    path('portfolio/', PortfolioFeedView.as_view(), name='portfolio-portfolio'),
    path('education/', EducationFeedView.as_view(), name='portfolio-education'),
    path('skills/', SkillsFeedView.as_view(), name='portfolio-skills'),
]
