from django.contrib import admin
from django.urls import path
from .views import FileDownloadAPIView, FileUploadAPIView, FileListAPIView

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view(), name="file_upload" ),
    path('download/<str:file_name>/', FileDownloadAPIView.as_view(), name="file_download"),
    path('', FileListAPIView.as_view(), name="file_list")
]