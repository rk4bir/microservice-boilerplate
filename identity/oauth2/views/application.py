from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.models import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from oauth2_provider.views.application import ApplicationOwnerIsUserMixin
from oauth2_provider.models import get_application_model

from .mixins import IsSuperUserMixin


def get_application_form():
    """Returns the form class for the application model"""
    select_input_widget = forms.Select(attrs={'class': "form-control"})
    return modelform_factory(
        get_application_model(),
        fields=(
            "name", "client_id", "client_secret", "client_type",
            "authorization_grant_type", "redirect_uris"
        ),
        widgets={
            'name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Application name",
                    "onblur": "this.placeholder='Application name'",
                    "onfocus": "this.placeholder=''"
                }
            ),
            'client_id': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Client ID",
                    "onblur": "this.placeholder='Client ID'",
                    "onfocus": "this.placeholder=''"
                }
            ),
            'client_secret': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Client Secret",
                    "onblur": "this.placeholder='Client Secret'",
                    "onfocus": "this.placeholder=''"
                }
            ),
            'client_type': select_input_widget,
            'authorization_grant_type': select_input_widget,
            'redirect_uris': forms.Textarea(attrs={
                "placeholder": "Redirect url",
                "onblur": "this.placeholder='Redirect url'",
                "onfocus": "this.placeholder=''",
                'class': 'form-control',
                'style': 'height: 100px'
            })
        }
    )


class ApplicationRegistration(IsSuperUserMixin, LoginRequiredMixin, CreateView):
    """
    View used to register a new Application for the request.user
    """
    template_name = "oauth2/application_registration_form.html"

    def get_form_class(self):
        """Returns the form class for the application model"""
        return get_application_form()

    def get_success_url(self):
        """Returns success url"""
        return reverse_lazy("oauth2:apps")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ApplicationDetail(IsSuperUserMixin, ApplicationOwnerIsUserMixin, DetailView):
    """
    Detail view for an application instance owned by the request.user
    """
    context_object_name = "application"
    template_name = "oauth2/application_detail.html"


class ApplicationList(IsSuperUserMixin, ApplicationOwnerIsUserMixin, ListView):
    """
    List view for all the applications owned by the request.user
    """
    context_object_name = "applications"
    template_name = "oauth2/application_list.html"


class ApplicationDelete(IsSuperUserMixin, ApplicationOwnerIsUserMixin, DeleteView):
    """
    View used to delete an application owned by the request.user
    """
    context_object_name = "application"
    success_url = reverse_lazy("oauth2:apps")
    template_name = "oauth2/application_confirm_delete.html"


class ApplicationUpdate(IsSuperUserMixin, ApplicationOwnerIsUserMixin, UpdateView):
    """
    View used to update an application owned by the request.user
    """
    context_object_name = "application"
    template_name = "oauth2/application_form.html"

    def get_form_class(self):
        """
        Returns the form class for the application model
        """
        return get_application_form()
