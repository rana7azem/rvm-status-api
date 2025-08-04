from rest_framework import serializers
from .models import RVM

class RVMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RVM
        fields = '__all__'
