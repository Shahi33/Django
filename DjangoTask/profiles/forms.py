
from django import forms
from .models import SkillSet,Profile

class SkillSetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SkillSetForm, self).__init__(*args,**kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control'
            })
        
    class Meta:
        model = SkillSet
        exclude = ('profile',)

class ProfileForm(forms.ModelForm):
    extra_field_count = forms.CharField(widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(ProfileForm, self).__init__(*args,**kwargs)
        self.fields['extra_field_count'].initial = extra_fields
        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = forms.CharField()

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control'
            })
        
    class Meta:
        model = Profile
        fields = ("__all__")



