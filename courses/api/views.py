from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer

class SubjectListView(generics.ListAPIView):
	queryset 			=	Subject.objects.all()
	serializer_class	=	SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
	queryset 			=	Subject.objects.all()
	serializer_class	=	SubjectSerializer

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response 
from ..models import Course
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CourseEnrollView(APIView):
	authentication_classes 	=	(BasicAuthentication,)
	permissions_classes 	=	(IsAuthenticated,)

	def post(self,request,pk,format=None):
		course = get_object_or_404(Course,pk=pk)
		course.students.add(request.user)
		return Response({'enrolled':True})

from rest_framework import viewsets
from .serializers import CourseSerializer
from .permissions import IsEnrolled
from .serializers import CourseWithContentsSerializer
from rest_framework.decorators import action

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
	queryset 			=	Course.objects.all()
	serializer_class	=	CourseSerializer

	@action(detail=True,methods=['get'],serializer_class=CourseWithContentsSerializer,authentication_classes=[BasicAuthentication],permission_classes=[IsAuthenticated,IsEnrolled])

	def contents(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def enroll(self,request,*args,**kwargs):
		course 			=	self.get_object()
		course.students.add(request.user)
		return Response({'enrolled':True})
