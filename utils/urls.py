from django.urls import path

from .views import SimditorFileUploadAPIView, SimditorImageUploadAPIView

urlpatterns = [
    path("upload_image/", SimditorImageUploadAPIView.as_view(), name="upload_image"),
    path("upload_file/", SimditorFileUploadAPIView.as_view(), name="upload_file")
]
