from assets.models import *
from django.contrib import admin
'''from assets.models import UserProfile


# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
'''

def reg(mod):
    admin.site.register(mod)


reg(Asset)
reg(AssetCheckout)
reg(AssetType)
reg(AssetMake)
reg(AssetModel)
reg(Location)
