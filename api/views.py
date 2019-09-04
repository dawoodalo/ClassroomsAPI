from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from classes.models import Classroom
from .serializers import ClassroomSerializer, ClassroomDetailsSerializer, UpdateClassroomSerializer


class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'Classroom_id'


class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateClassroomSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'Classroom_id'


class CancelClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'Classroom_id'


class ClassroomCreate(CreateAPIView):
	serializer_class = UpdateClassroomSerializer

	def perform_create(self, serializer):
		serializer.save(teacher = self.request.user)