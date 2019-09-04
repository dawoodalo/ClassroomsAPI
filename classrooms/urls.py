
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api import views as api_views
from classes import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('apiclassroom/', api_views.ClassroomList.as_view(), name="apiclassrooms-list"), 
    path('apiclassroom/<int:classroom_id>/', api_views.ClassroomDetails.as_view(), name="apiclassroom-details"),
    path('apiclassroom/<int:classroom_id>/update/', api_views.UpdateClassroom.as_view(), name="update-apiclassroom"),
    path('apiclassroom/<int:classroom_id>/cancel/', api_views.CancelClassroom.as_view(), name="cancel-apiclassroom"),
    path('apicreate/', api_views.ClassroomCreate.as_view(), name="apicreate classroom"),

    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh")
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
