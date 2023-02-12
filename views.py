from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
import sqlite3
import json 
import random
from pathlib import Path

from .serializers import ngoSerializer,philSerializer,NameSerializer,checkDataSerializer
from .models import NgoDB,philDB
# BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
class PhilRegisterViewSet(viewsets.ModelViewSet):
    queryset = philDB.objects.all()
    serializer_class = philSerializer
    
class NgoRegisterViewSet(viewsets.ModelViewSet):
    queryset = NgoDB.objects.all()
    serializer_class = ngoSerializer

class favNgo(APIView):
    def post(self, request, format=None):
        con = sqlite3.connect(r"C:\Varun\Programing\hackathon\newProject\db.sqlite3")
        cur = con.cursor()
        serializer = NameSerializer(data=request.data) #Username is entered here
        if serializer.is_valid():
            e = serializer.data.get('cphil')
            print("hellooo")
            areaOfInterest = ""
            for row in cur.execute('SELECT phil_name,phil_interest FROM ngo_phildb;'):
                if e == row[0]:
                    x = row[1]
            areaOfInterest = x.split(",")
            print(areaOfInterest)
            cur1 = con.cursor()
            ngoNames = ""
            while(ngoNames == ""):
                random_choice = random.choice(areaOfInterest)
                for row in cur1.execute('SELECT ngo_sector,ngo_name FROM ngo_ngodb'):
                    if row[0] == random_choice:
                        print("hii")
                        ngoNames = ngoNames + "," + row[1]                    
            # json_object = json.dumps(interestNgo) 
        return Response(ngoNames)
    
class ngoDetailsViewSet(APIView):
    def post(self, request, format=None):
        con = sqlite3.connect(r"C:\Varun\Programing\hackathon\newProject\db.sqlite3")
        cur = con.cursor()
        serializer = NameSerializer(data=request.data) #Ngo Details is obtained from ngo name
        if serializer.is_valid():
            e = serializer.data.get('cphil')
            for row in cur.execute('SELECT ngo_name,ngo_goal,ngo_loc,ngo_sector FROM ngo_ngodb'):
                if e == row[0]:
                    print(row)
                    return JsonResponse({
                        "name" : row[0],
                        "goal" : row[1],
                        "loc" : row[2],
                        "sector" : row[3],
                    })
        return Response("Ngo not found")


class SearchedNgo(APIView):
    def post(self, request, format=None):   
        con = sqlite3.connect(r"C:\Varun\Programing\hackathon\newProject\db.sqlite3")
        cur = con.cursor()   
        ngoNames = ""            
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            e = serializer.data.get('cphil')
            for row in cur.execute('SELECT ngo_name FROM ngo_ngodb'):
                print(row[0].find(e))
                if row[0].find(e) != -1:
                    ngoNames = ngoNames + "," + row[0]
        return Response(ngoNames)
      
class UserViewset(APIView):
  def post(self, request, format=None):
    con = sqlite3.connect(r"C:\Varun\Programing\hackathon\newProject\db.sqlite3")
    cur = con.cursor()    
    serializer = NameSerializer(data=request.data)
    if serializer.is_valid():
      e = serializer.data.get('cphil')
      for row in cur.execute('SELECT phil_name,phil_interest,phil_email,phil_phoneNo FROM ngo_phildb;'):
        if e == row[0]:
          return JsonResponse({
            "i" : row[1],
            "e" : row[2],
            "ph" : row[3],
          })
    return Response("")
    
class checkData(APIView):
    def post(self, request, format=None):
      con = sqlite3.connect(r"C:\Varun\Programing\hackathon\newProject\db.sqlite3")
      cur = con.cursor()
      a = 0
      b = 0
      print("Inside checkData")
      serializer = checkDataSerializer(data=request.data)
      if serializer.is_valid():
        print("hello")
        n = ""
        e = serializer.data.get('cemail')
        p = serializer.data.get('cpwd')
        print(e)
        for row in cur.execute('SELECT phil_email,phil_pass FROM ngo_phildb;'):
          if row[0] == e:
            print(row[0])
            a = 1
            break
        for row in cur.execute('SELECT phil_pass,phil_name FROM ngo_phildb;'):
          if row[0] == p:
            b = 1
            n = row[1]
            break
        if a == 1 and b == 1:
          print("Correct ans")
          return JsonResponse({"ans":"right","type":"phil","name":n})
        else:
          print("Wrong Ans")
          return JsonResponse({"ans":"wrong"})
      else:
        return Response("Error")
            
def search(request):
  template = loader.get_template('search.html')
  return HttpResponse(template.render())   

def register(request):
  template = loader.get_template('Registration.html')
  return HttpResponse(template.render())   
     
def philLogin(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())     

def ngoLogin(request):
  template = loader.get_template('loginngo.html')
  return HttpResponse(template.render())     
    
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def profile(request):
  template = loader.get_template('profile.html')
  return HttpResponse(template.render())

def fakepage(request):
  template = loader.get_template('ngofakecd1.html')
  return HttpResponse(template.render())

def pay(request):
  template = loader.get_template('pay4.html')
  return HttpResponse(template.render())

def upi(request):
  template = loader.get_template('pay2.html')
  return HttpResponse(template.render())
