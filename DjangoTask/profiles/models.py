from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.




class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(upload_to='cv/')
    photo = models.ImageField(upload_to='photo/')
    # skill = models.ForeignKey(SkillSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def choices(self):
        return self.skillset_set.all()

class SkillSet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    skill_name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField()

    def __str__(self):
        return self.skill_name

    def get_absolute_url(self):
        return reverse ('profiles:post-detail', kwargs = {'pk':self.pk})

    @receiver(post_delete, sender=Profile)
    def delete_skill(sender, instance, **kwargs):
        
        SkillSet.objects.filter(profile = instance.id).delete()

