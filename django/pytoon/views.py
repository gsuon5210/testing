from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['1', '2', '3', 'ㅁㅁ']
    })