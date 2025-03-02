from django.urls import path
from .views import upload_and_process_file, home,success_view  # Ensure these views exist

urlpatterns = [
    path("", home, name="home"),  # Root URL
    path("upload/", upload_and_process_file, name="file_upload"),
     path("success/", success_view, name="success_page"),
]
