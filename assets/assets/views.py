from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

from assets.models import Asset
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


def index(request, model='asset'):
    model = modelModels['asset']()
    model_fields = model._meta.get_all_field_names()
    return render_to_response(
        'index.html',
        {
            'model_fields': model_fields,
        },
        context_instance=RequestContext(request))


def ajax_search(request, model='asset'):
    model = modelModels['asset']
    model_instance = model()
    model_fields = model_instance._meta.get_all_field_names()

    num_results = 0

    results = model.objects
    filter_counter = 0
    for field in model_fields:
        try:
            kwargs = {
                field + '__contains': request.REQUEST[field]
            }
            results = results.filter(**kwargs).order_by('id')
            filter_counter += 1
        except TypeError:  # related field or something
            pass
        except KeyError:  # (not defined by the client)
            pass

    if filter_counter == 0:
        results = model.objects.all()

    try:
        results = results[:100]
    except TypeError:
        results = results.all()[:100]

    num_results = model.objects.count()

    try:
        data = serializers.serialize('json', results)
    except TypeError:  # we ended up with no usable filters
        data = '[]'

    # data = "[{'num_results': '" + str(num_results) + "'}]," + data

    return HttpResponse(data, mimetype="application/json")



def create_object(request, model):

    check_form(model)

    object_template = 'generic/model-form.html'
    form = modelForms[model]()

    if request.method == 'POST':
        form = modelForms[model](request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    extra_js = ['object-form.js']
    extra_style = ['object-form.css']

    return render_to_response(
        'generic/model.html',
        {
            'form': form,
            'model': model,
            'extra_js': extra_js,
            'extra_style': extra_style,
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
    extra_js = []

    return render_to_response(
        'generic/model.html',
        {
            'id': ID,
            'qr': qr_base64,
            'qr_url': '',
            'form': form,
            'model': model,
            'extra_style': extra_style,
            'extra_js': extra_js,
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
    extra_js = ['object-form.js']

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
            'extra_js': extra_js,
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
