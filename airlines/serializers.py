#!/usr/bin/python
# -*- coding: utf8 -*-


from rest_framework import serializers
from airlines.models import Airport, Airliner


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('id', 'name', 'title')


class AirlinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airliner
        fields = ('id', 'name', 'title')
