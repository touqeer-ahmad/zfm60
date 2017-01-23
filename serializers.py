# Serializers for mode and state REST services - serializers.py

from myapp.models import enroll
from rest_framework import serializers

class enrollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = enroll
        fields = ('url', 'event')
