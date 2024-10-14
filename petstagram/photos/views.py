from django.shortcuts import render, redirect
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.count()
    comments = photo.comment_set.count()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }


    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk: int):
    photo = Photo.objects.get(pk=pk)

    if request.method == "GET":
        form = PhotoEditForm(instance=photo)

    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details-photo', pk=pk)

    context = {
        'form': form
    }


    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')
