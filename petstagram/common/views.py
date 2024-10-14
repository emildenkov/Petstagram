from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def home_page(request):

    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    like_object = Like.objects.filter(
        to_photo_id=photo_id
    ).first()

    if like_object:
        like_object.delete()
    else:
        like = Like(to_photo=photo_id)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo_details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')