# serializers.py
from rest_framework import serializers

from .models import *

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name', 'alias')

class SampleCheck(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ( 'name', 'alias')


class Login(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('uid','pwd','otp','token')