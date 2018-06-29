import json

import django
from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import generics as rest_framework_generics
from django.db import connection
from django.template import loader

from airlines.models import Airport, Airliner
from airlines.serializers import AirportSerializer, AirlinerSerializer


class AirportList(rest_framework_generics.ListCreateAPIView):
    queryset = Airport.objects.all()

    serializer_class = AirportSerializer


class AirlinerList(rest_framework_generics.ListCreateAPIView):
    queryset = Airliner.objects.all()

    serializer_class = AirlinerSerializer


def index(request):
    template = loader.get_template('airlines/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def arrival_count(request):
    airliner_id = request.GET.get('airliner_id')
    airport_id = request.GET.get('airport_id')

    if not airliner_id or not airport_id:
        data = {'count': -1}
        return HttpResponse(json.dumps(data), content_type='application/json')

    con = django.db.connection
    with con.cursor() as cursor:
        cursor.execute('select arrival_count({}, {});'.format(airliner_id, airport_id))
        val = cursor.fetchone()[0]

    data = {'count': val}
    return HttpResponse(json.dumps(data), content_type='application/json')
