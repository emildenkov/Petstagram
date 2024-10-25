from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetDeleteForm, PetAddForm, PetEditForm
from petstagram.pets.models import Pet


class AddPetView(CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('details-profile', kwargs={'pk': 1})


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm
    success_url = reverse_lazy('details-profile', kwargs={'pk': 1})
    slug_url_kwarg = 'pet_slug'

    def get_initial(self):
        return self.get_object().__dict__


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })
        return kwargs


class EditPetView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy(
            'details-pet',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug'],
            }
        )


class DetailsPetView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_photos'] = context['pet'].photo_set.all()
        context['comment_form'] = CommentForm()

        return context
