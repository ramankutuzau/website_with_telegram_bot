import asyncio
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *
from gallery.jobs.jobs import send_sms_bot


# Create your views here.


def index(request):
    projects = Projects.objects.all()
    return render(request, 'index.html', {'projects': projects})

@csrf_exempt
def send_instagram(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        button_name = data.get('button_name')
        asyncio.run(send_sms_bot(f"Переход в инстаграмм: {button_name}"))

    return JsonResponse({'error': 'Invalid request method'})



