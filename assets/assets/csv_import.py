from django.db.utils import *

from models import *
from forms import *

import csv
import re


def csv_import(request, uploaded_file_name, model_name):

    model = modelModels[model_name]
    model_form = modelForms[model_name]().fields

    returns = 0
    fields_not_found = []
    objects = []

    headers = []
    try:	
      with open(uploaded_file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        first = True
        for row in reader:
            # First row is headers
            if first:
                first = False
                for field in model_form:
                    if [s for s in row if field not in s] and model_form[field].required:
                        fields_not_found.append(field)
                    headers = row
                    tmp = []
                    for header in headers:
                        tmp.append(re.sub(r',$', '', header))
                    headers = tmp
                if fields_not_found != []:
                    returns = 1
                    break
            else:
                i = 0
                obj = model()
                for header in headers:
                    value = re.sub(r',$', '', row[i])
                    setattr(obj, field, value)
                    i += 1
                print obj
                objects.append(obj)

        try:
            model.objects.bulk_create(objects)
        except IntegrityError:
            #  Since our bulk import failed, we've got to import our objects one by one
            print 'bulk import failed! trying to import individually'
            for mobject in objects:
                try:
                    mobject.save()
                except:
                    mobject.clean()
                    try:
                        mobject.validate_unique()
                    except TypeError:
                        print 'object field is the wrong type!'
	
    except Error:
	  print 'Motherfucking problems'
	
    return {
        'returns': returns,
        'fields_not_found': fields_not_found,
        'headers': headers,
        'objects_inserted': objects,
    }
	
def related_import(request):
    pass
