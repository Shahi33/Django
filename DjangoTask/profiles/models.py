from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.




class Profile(models.Model):
    '''Profile models'''
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(upload_to='cv/')
    photo = models.ImageField(upload_to='photo/')


    def __str__(self):
        return self.name
    def choices(self):
        return self.skillset_set.all()

class SkillSet(models.Model):
    '''SkillSet models with foreign key profile'''
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    skill_name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField()

    def __str__(self):
        return self.skill_name

    def get_absolute_url(self):
        return reverse ('profiles:post-detail', kwargs = {'pk':self.pk})


    @receiver(post_delete, sender=Profile)
    def delete_skill(sender, instance, **kwargs):
        '''delete skill when profile is deleted'''
        SkillSet.objects.filter(profile = instance.id).delete()

