'''
Register models in admin
'''

from django.contrib import admin
from .models import SkillSet, Profile

class AdminSkillSet(admin.ModelAdmin):
    model = SkillSet
    list_display = ('id','profile','skill_name','proficiency_level',)

class AdminProfile(admin.ModelAdmin):
    model = Profile
    list_display = ('id','name','email','cv','photo')


admin.site.register(
    SkillSet, AdminSkillSet
    )

admin.site.register(
    Profile, AdminProfile
    )