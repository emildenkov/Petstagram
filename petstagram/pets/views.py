from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetDeleteForm, PetAddForm, PetEditForm
from petstagram.pets.models import Pet


def add_pet(request):
    form = PetAddForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('details-profile', pk=1)

    context = {
        'form': form
    }


    return render(request, 'pets/pet-add-page.html', context)


def delete_pet(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('details-profile', pk=1)

    context = {
        'form': form,
        'pet': pet
    }

    return render(request, 'pets/pet-delete-page.html', context)


def edit_pet(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details-pet', username=username, slug=slug)

    context = {
        'form': form,
        'pet': pet
    }

    return render(request, 'pets/pet-edit-page.html', context)


def details_pet(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    all_photos = pet.photos.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form
    }

    return render(request, 'pets/pet-details-page.html', context)