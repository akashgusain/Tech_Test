from rest_framework import routers
from teacher_db.views import TeacherViewSet, UploadViewSet

router = routers.SimpleRouter()

router.register(r'teachers', TeacherViewSet)
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = router.urls
