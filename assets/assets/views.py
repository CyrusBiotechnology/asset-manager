from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
#from django.db.models import Q
#results = Asset.objects.filter(Q(description=query) | Q(external_id=query) | Q(serial_number=query)).order_by('id')

from assets.models import Asset


def index(request):
    return render_to_response(
        'index.html',
        {},
        context_instance=RequestContext(request))


def ajax_search(request):
    query = request.GET.get('q', '')
    if(query == ''):
        return HttpResponseBadRequest()

    results = Asset.objects.filter(description__contains=query).order_by('id')

    data = serializers.serialize('json', results)
    return HttpResponse(data, mimetype="application/json")
