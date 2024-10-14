from django.shortcuts import render, redirect

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

    if request.method == 'GET':
        form = PetEditForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details-pet', username=username, slug=slug)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-edit-page.html', context)


def details_pet(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    all_photos = pet.photos.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)