from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.base import View

from account.forms import CustomUserCreationForm

__all__ = [
    'home',
    'all_works',
    'work',
    'make_mailing',
    'blog',
    'detail_post',

]

from portfolio.controllers import mailing_data

from portfolio.forms import MailingForm

from portfolio.models import Assets, Work, Render, Post


def home(request):
    return render(request, 'portfolio/home.html')


def all_works(request):
    qs = Assets.objects.all()
    ln = len(qs)
    for i in range(0, ln):
        qs[i].image = str(qs[i].image)[17:]
    context = {
        'qs': qs
    }
    return render(request, 'portfolio/all_works.html', context)


# class WorkDetailView(DetailView):
#     template_name = 'portfolio/detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context[''] =
#         return context

def work(request, pk=None):
    qs_asset = Assets.objects.filter(id=pk)
    qs_work = Work.objects.filter(asset_id=pk)
    qs_render = Render.objects.filter(asset_id=pk)
    ln = len(qs_asset)
    for i in range(0, ln):
        qs_asset[i].image = str(qs_asset[i].image)[17:]
    ln = len(qs_render)
    for i in range(0, ln):
        qs_render[i].render_image_path = str(qs_render[i].render_image_path)[17:]
    context = {
        'qs_asset': qs_asset,
        'qs_work': qs_work,
        'qs_render': qs_render
    }
    return render(request, 'portfolio/detail.html', context)


def xz(request):
    context = {
        'qs_asset': 1,
        'qs_work': 2,
        'qs_render': 3
    }
    return JsonResponse(context)


def make_mailing(request, pk=None):
    if pk is not None:
        asset = Assets.objects.filter(id=pk)
        work = Work.objects.filter(asset_id=pk)
        context = {
            'asset': asset,
            'work': work,
        }

        asset = Assets.objects.filter(id=pk)
        return JsonResponse({'asset': list(asset)})

    else:
        if request.method == 'POST':
            form = MailingForm(request.POST)
            print(3)
            if form.is_valid():
                print(1)
                context = mailing_data(form.cleaned_data)
                return render(request, 'portfolio/mailing.html', context)
            else:
                print(form.errors)
                return render(request, 'portfolio/mailing.html', {'form': form})
        else:
            form = MailingForm()
            return render(request, 'portfolio/mailing.html', {'form': form})


def blog(request):
    qs = Post.objects.all()
    context = {
        'post_list': qs
    }
    return render(request, 'portfolio/blog.html', context)


def detail_post(request, pk=None):
    qs_post = Post.objects.filter(id=pk)
    context = {
        'qs_post': qs_post
    }
    return render(request, 'portfolio/detail_post.html', context)
