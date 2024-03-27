from django.shortcuts import render

from core.models import Figurine


def index(request):
    figurines = Figurine.objects.all()

    context = {'figurines': figurines}
    return render(request, 'core/index.html', context=context)
