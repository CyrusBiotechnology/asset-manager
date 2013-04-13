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


modelModels = {
    'asset': Asset,
    'location': Location,
    'make': AssetMake,
    'model': AssetModel,
}


modelForms = {
    'asset': AssetForm,
    'location': LocationForm,
    'make': MakeForm,
    'model': ModelForm,
}


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


def edit_asset(request, aID):

    object_template = 'assets/asset-form.html'
    asset = get_object_or_404(Asset, pk=aID)
    form = AssetForm(instance=asset)

    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    return render_to_response(
        'assets/asset.html',
        {'form': form,
        'object_template': object_template},
        context_instance=RequestContext(request))


def create_object(request, model):

    check_form(model)

    object_template = 'generic/model-form.html'
    form = modelForms[model]()

    if request.method == 'POST':
        form = modelForms[model](request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    return render_to_response(
        'generic/model.html',
        {
            'form': form,
            'model': model,
            'object_template': object_template
        },
        context_instance=RequestContext(request)
    )


def display_object(request, ID, model):

    check_model(model)

    object_template = 'generic/model-display.html'
    model_object = modelModels[model]
    model_object = get_object_or_404(model_object, pk=ID)
    form = modelForms[model](instance=model_object)

    qr_base64 = get_qrcode()

    extra_style = ['object.css']

    return render_to_response(
        'generic/model.html',
        {
            'id': ID,
            'qr': qr_base64,
            'qr_url': '',
            'form': form,
            'model': model,
            'extra_style': extra_style,
            'object_template': object_template,
        },
        context_instance=RequestContext(request)
    )


def edit_object(request, ID, model):

    check_model(model)

    object_template = 'generic/model-form.html'
    model_object = modelModels[model]
    model_object = get_object_or_404(model_object, pk=ID)
    form = modelForms[model](instance=model_object)

    extra_style = ['object.css']

    if request.method == 'POST':
        form = modelForms[model](request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    return render_to_response(
        'generic/model.html',
        {
            'id': ID,
            'form': form,
            'model': model,
            'extra_style': extra_style,
            'object_template': object_template,
        },
        context_instance=RequestContext(request)
    )


def check_model(model):
    try:
        modelModels[model]()
    except KeyError:
        return HttpResponseBadRequest()


def check_form(model):
    try:
        modelForms[model]()
    except KeyError:
        return HttpResponseBadRequest()


def get_qrcode():
    output = StringIO.StringIO()  # This is sort of like temp, but suaver
    #qr_url = HOSTNAME + reverse('assets', kwargs={'aID': aID})
    qr_url = ''
    qr_url = qr_url.lower()
    img = qrcode.make(qr_url)
    img.save(output, 'gif')
    img = output.getvalue().encode('base64')
    return img
