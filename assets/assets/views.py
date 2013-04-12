from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers
#from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse

#from django.db.models import Q
#results = Asset.objects.filter(Q(description=query) | Q(external_id=query) | Q(serial_number=query)).order_by('id')

from settings import HOSTNAME
from assets.models import Asset  # , AssetMake, AssetModel
from assets.forms import *

# Third party libraries
import qrcode

# Builtins
import StringIO


def dummy(request):
    return('')


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


def create_asset(request):
    display_template = 'assets/asset-form.html'
    form = AssetForm()
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    return render_to_response(
        'assets/asset.html',
        {'form': form,
        'display_template': display_template},
        context_instance=RequestContext(request))


def asset(request, aID):

    display_template = 'assets/asset-display.html'
    asset = get_object_or_404(Asset, pk=aID)
    form = AssetForm(instance=asset)
    '''
    try:
        model = AssetModel(asset.model)
        make = AssetMake(model.make)
    except ObjectDoesNotExist:
        pass
    '''

    output = StringIO.StringIO()  # This is sort of like temp, but suaver
    qr_url = HOSTNAME + reverse('asset', kwargs={'aID': aID})
    qr_url = qr_url.lower()
    img = qrcode.make(qr_url)
    img.save(output, 'gif')
    img = output.getvalue().encode('base64')

    return render_to_response(
        'assets/asset.html',
        {'form': form,
        'display_template': display_template,
        'qr': img,
        'qr_url': qr_url,
        'id': aID
        },
        context_instance=RequestContext(request))


def edit_asset(request, aID):

    display_template = 'assets/asset-form.html'
    asset = get_object_or_404(Asset, pk=aID)
    form = AssetForm(instance=asset)

    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    return render_to_response(
        'assets/asset.html',
        {'form': form,
        'display_template': display_template},
        context_instance=RequestContext(request))
