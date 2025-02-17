from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy


from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


class HomePageView(ListView):
    template_name = 'common/home-page.html'
    model = Photo
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('name')

        if pet_name:
            queryset = queryset.filter(
                tagged_pets__name__icontains=pet_name
            )

        return queryset


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


def add_comment(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')