from rest_framework import serializers
from .models import *


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id','username','email','role','password']
        extra_kwargs = {'password': {'write_only':True}}

class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'