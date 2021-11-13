from django.urls import path
from rest_framework.fields import CreateOnlyDefault
from .views import JobListView, JobDetailView, JobCreateView

urlpatterns = [
    path("", JobListView.as_view()),
    path("<int:job_id>/", JobDetailView.as_view()),
    path("create/", JobCreateView.as_view()),
]
