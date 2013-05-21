from assets.models import *
from django.contrib import admin
#from assets.models import UserProfile


'''
# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
'''


def reg(mod):
    for i in mod:
        admin.site.register(i)


reg([
  Asset,
  AssetCheckout,
  AssetType,
  AssetModel,
  Location,
])



class ModelInline(admin.StackedInline):
    model = AssetModel
    extra = 0

class MakeAdmin(admin.ModelAdmin):
    inlines = [ModelInline,] # allows you to add links in admin on the same page as the slide
admin.site.register(AssetMake, MakeAdmin)

