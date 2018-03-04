from datetime import datetime

from django.http import JsonResponse
from django.http import Http404
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt

from .models import *


def get_note_list(request):
    response = {'notes': []}

    if request.method == 'GET':
        qid = request.GET.get('qid', '')

        if qid == '':
            qid_found = Note.objects.all().aggregate(Max('qid'))
            qid_max = qid_found.get('qid__max')
            if qid_max is None:
                qid = 0
            else:
                qid = qid_max + 1

        try:
            qid = int(qid)
        except Exception:
            return JsonResponse(response)

        response = {
            'notes': [obj for obj in Note.objects.filter(qid=qid)]
        }

    return JsonResponse(response)


@csrf_exempt
def add_note(request):
    if request.method == 'POST':
        form = NoteAddForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.date = datetime.now()
            req.save()
        return JsonResponse(None)

    else:
        raise Http404("No such page exists")


@csrf_exempt
def delete_note(request):
    if request.method == 'POST':
        try:
            obj = Note.objects.filter(id=int(request.POST.get('id')))
            obj.delete()
        except Exception:
            pass
        return JsonResponse(None)

    else:
        raise Http404("No such page exists")

