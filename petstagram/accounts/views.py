from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login-page.html')


def delete_profile_page(request, pk: int):
    return render(request, 'accounts/profile-delete-page.html')


def details_profile_page(request, pk: int):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile_page(request, pk: int):
    return render(request, 'accounts/profile-edit-page.html')


def register(request):
    return render(request, 'accounts/register-page.html')
