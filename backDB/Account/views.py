from django.shortcuts import render
from rest_framework import generics, filters
from .models import College, Students, Professors
from .serializers import Collegeserializer, Professorserializer, Studentserializer
# Create your views here.

class ListColleges(generics.ListCreateAPIView):
    # search_fields = ['name']
    # filter_backends = (filters.SearchFilter,)
    queryset = College.objects.all()
    serializer_class = Collegeserializer

class DetailColleges(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = Collegeserializer



class ListStudents(generics.ListCreateAPIView):
    search_fields = ['name', '=semester', '=enrollment', 'department','college__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Students.objects.all()
    serializer_class = Studentserializer

class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentserializer



class ListProfessors(generics.ListCreateAPIView):
    search_fields = ['name','department', '=role','college__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Professors.objects.all()
    serializer_class = Professorserializer

class DetailProfessors(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer