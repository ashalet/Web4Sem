from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from portfolio.models import Assets, Work

__all__ = (
    "mailing_view",

)


# class MailingAPIView(APIView):
#     # def __init__(self, pk):
#     #     super(MailingAPIView, self).__init__()
#     #     self.pk = pk
#
#     def get(self, request):
#         print(request)
#         asset = Assets.objects.filter(id=request.pk).values()
#         work = Work.objects.filter(id=request.pk).values()
#         return Response({'asset': list(asset), 'work': list(work)})

def mailing_view(request, pk=None):
    if pk is not None:
        asset = Assets.objects.filter(id=pk).values()
        work = Work.objects.filter(id=pk).values()
        return JsonResponse({'asset': list(asset), 'work': list(work)})
    else:
        asset = Assets.objects.all().values()
        work = Work.objects.all().values()
        return JsonResponse({'asset': list(asset), 'work': list(work)})