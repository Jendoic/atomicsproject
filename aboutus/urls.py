from django.urls import path

from .views import AboutPageListView, AboutPageDetailView, StaffPageListView

urlpatterns = [
    path("", AboutPageListView.as_view(), name="aboutpage_list"),
    path("<uuid:pk>", AboutPageDetailView.as_view(), name="aboutpage_detail"),
    path("staffpage/", StaffPageListView.as_view(), name="staffpage"),
]
