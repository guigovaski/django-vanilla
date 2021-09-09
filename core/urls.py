from django.urls import path

from .views import IndexView, DownloadView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('download/', DownloadView.as_view(), name='download'),
]
