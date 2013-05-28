from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

from assets.models import *
from assets.forms import *
from csv_import import *

# Third party libraries
import qrcode

# Builtins
import StringIO


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


def list(request, model='asset', page=0):
    template = 'list.html'
    limit = 100
    start = page * limit
    model_instances = modelModels[model].objects.all()
    model_instance = modelModels[model]()
    model_fields = model_instance._meta.get_all_field_names()
    forms = []

    try:
        request.REQUEST['ajax']
        template = 'list-partial.html'
    except KeyError:
        pass

    for field in model_fields:
        try:
            if request.REQUEST[field] == 'asc':
                model_instances = model_instances.order_by('-' + field)
            elif request.REQUEST[field] == 'desc':
                model_instances = model_instances.order_by(field)
        except KeyError:
            continue

    model_instances[start:limit]

    for obj in model_instances:
        forms.append(modelForms[model](instance=obj))

    return render_to_response(
        template,
        {
            'forms': forms,
        },
        context_instance=RequestContext(request)
    )


def ajax_search(request, model='asset'):
    model = modelModels['asset']
    model_instance = model()
    model_fields = model_instance._meta.get_all_field_names()

    num_results = 0

    results = model.objects
    filter_counter = 0

    for field in model_fields:
        #search_all_fields(results=results, field=field, filter_counter=filter_counter)
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


def import_model(request, model):
    title = 'Importing ' + model + 's'
    template = 'import/import.html'
    sub_template = 'import/model.html'
    model_form = modelForms[model]()
    upload_form = ImportFileForm()
    fields_not_found = []
    objects_inserted_forms = []
    headers = []

    if request.method == 'POST':
        upload_form = ImportFileForm(request.POST, request.FILES)
        upload_form.is_valid()
        upload = ImportFile(**upload_form.cleaned_data)
        upload.save()
        csv_import_output = csv_import(request, upload.uploaded.name, model)
        if csv_import_output['returns'] == 1:
            fields_not_found = csv_import_output['fields_not_found']
            upload.uploaded.delete()
            upload.delete()
        else:
            sub_template = 'import/imported.html'
            title = 'Imported ' + model + 's'
            objects_inserted = csv_import_output['objects_inserted']
            headers = csv_import_output['headers']
            for obj in objects_inserted:
                objects_inserted_forms.append(modelForms[model](instance=obj))

    return render_to_response(
        template,
        {
            'model': model,
            'model_form': model_form,
            'upload_form': upload_form,
            'title': title,
            'headers': headers,
            'fields_not_found': fields_not_found,
            'sub_template': sub_template,
            'objects_inserted_forms': objects_inserted_forms,
        },
        context_instance=RequestContext(request)
    )


def import_index(request):
    title = 'Please choose a model'
    sub_template = 'import/index.html'
    return render_to_response(
        'import/import.html',
        {
            'models': modelModels,
            'title': title,
            'sub_template': sub_template,
        },
        context_instance=RequestContext(request))


def create_object(request, model):

    check_form(model)

    object_template = 'generic/model-form.html'

    if model == 'checkout':
        try:
            asset = request.REQUEST['asset']
            form = modelForms[model](initial={
                'asset': asset
            })
        except:
            form = modelForms[model]()
    else:
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

    qr_base64 = get_qrcode(request)

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


def search_all_fields(**kwargs):
    try:
        kwargs = {
            field + '__contains': request.REQUEST[field]
        }
        results = results.filter(**kwargs).order_by('id')
        filter_counter += 1
    except TypeError:  # related field or something
        raise TypeError
    except KeyError:  # (not defined by the client)
        raise KeyError
    return {
        'results': results,
        'filter_counter': filter_counter,
    }


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


def get_qrcode(request):
    output = StringIO.StringIO()  # This is sort of like temp, but suaver
    qr_url = request.META['HTTP_HOST'] + request.META['PATH_INFO']
    qr_url = qr_url.lower()
    img = qrcode.make(qr_url)
    img.save(output, 'gif')
    img = output.getvalue().encode('base64')
    return img


def handler404(request):
    template = '404page.html'
