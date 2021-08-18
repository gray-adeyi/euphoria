from core import models
from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from . import models
from . import forms
# Create your views here.

class Index(FormView):
    template_name = 'core/index.html'
    form_class = forms.MessageForm
    
    model = models.Message

    def form_valid(self, form: forms.MessageForm) -> HttpResponse:
        messages.success(self.request, "Your message has been successfully sent")
        form.save()
        return redirect('core:index')

    def form_invalid(self, form: forms.MessageForm) -> HttpResponse:
        messages.error(self.request, "An error occured while trying to deliver your message. please try again")
        print("Form invalid was hit")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['site_info'] = models.SiteInfo.objects.first()
        return context