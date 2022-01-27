from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SkillSetForm, ProfileForm
from django.http import JsonResponse
from .models import SkillSet, Profile
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.views.generic import View

from django.http  import HttpResponse, HttpResponseRedirect


class ProfileListView(ListView):
    model = SkillSet
    template_name = 'profiles/index.html'
    context_object_name = 'posts'
    def get_context_data(self,**kwargs):
        context = super(ListView,self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/skillset_detail.html'
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        profile =Profile.objects.get(pk = pk)
        form = SkillSetForm()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['skills'] = SkillSet.objects.filter(profile = profile)
        context['form'] = form
        return context


class SkillCreateView(DetailView):
    model = SkillSet
    template_name = 'profiles/skillset_detail.html'
    # context_object_name = 'profiles'
    def post(self, request, id):
        # context = {}
        profile_id = id
        profile = Profile.objects.get(id=id)
        skill_name = request.POST.get('skill_name')
        proficiency_level = request.POST.get('proficiency_level')

        skill = SkillSet.objects.create(profile=profile,skill_name=skill_name,proficiency_level=proficiency_level )
        skill.save()

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)
    
        

class ProfileEditView(DetailView):
    model = Profile
    template_name = 'profiles/skillset_detail.html'
    # context_object_name = 'profiles'
    def post(self, request, id):


        # context = {}
        skill_id = id
        skill = SkillSet.objects.get(id=id)
        skill.skill_name = request.POST.get('skill_name')
        skill.proficiency_level = request.POST.get('proficiency_level')
        skill.save()

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

        return render(request, 'profiles:post-detail', context)



class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = '/'
    


class ProfileView(View):

    def get(self, request, id=None):
        if id:
            profile = get_object_or_404(Profile, id = id)
            profile_form = ProfileForm(instance = profile)
            skill_set = skill_set.objects.all()
            skill_set_forms = [SkillSetForm(prefix=str(skill_set.id),instance=skill_set) for skill_set in skill_sets]
        else:
            profile_form = ProfileForm(instance=Profile())
            skill_set_forms = [SkillSetForm(prefix=str(x),instance=SkillSet()) for x in range(1)]
            template = 'profiles/skillset_form.html'
        context = {'profile_form':profile_form, 'skill_set_forms':skill_set_forms}
        return render (request, template, context)

    def post(self, request, id=None):
        context = {}
        if id:
            return self.put(request, id)
        profile_form = ProfileForm(request.POST,request.FILES, instance=Profile())
        val = int(self.request.GET.get('range')) or 1
        skill_set_forms = [SkillSetForm(request.POST, prefix=str(x), instance=SkillSet()) for x in range(val)]

        if profile_form.is_valid() and [cf.is_valid() for cf in skill_set_forms]:
            new_poll = profile_form.save(commit=False)
            
            new_poll.save()
            for cf in skill_set_forms:
                new_skill = cf.save(commit=False)
                new_skill.profile = new_poll
                new_skill.save()
            return HttpResponseRedirect('/')
        context = {'profile_form': profile_form, 'skill_set_forms': skill_set_forms}
        return render(request, 'profiles/skillset_form.html', context)
