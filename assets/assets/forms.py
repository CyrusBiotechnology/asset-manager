from django.forms import ModelForm, FileField
from assets.models import Asset, Location, AssetMake, AssetModel

'''

Model forms. Keep 'em generic!

'''


class AssetForm(ModelForm):
    class Meta:
        model = Asset


class LocationForm(ModelForm):
    class Meta:
        model = Location


class MakeForm(ModelForm):
    class Meta:
        model = AssetMake


class ModelForm(ModelForm):
    class Meta:
        model = AssetModel


'''

Generic file import form

'''


class ImportForm(forms.Form):
    file_to_import = FileField()
