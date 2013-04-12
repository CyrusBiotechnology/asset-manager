from django.forms  import ModelForm
from assets.models import Asset

class AssetForm(ModelForm):
    class Meta:
        model = Asset
