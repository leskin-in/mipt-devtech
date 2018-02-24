from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from datetime import datetime
from django.db.models import Max


def view_note_queue(request):
    if request.method == 'POST':
        act = request.POST.get('action_type', None)
        if act == 'delete':
            try:
                obj = Note.objects.filter(id=int(request.POST.get('id')))
                obj.delete()
            except Exception:
                redirect('/')
        elif act == 'add':
            form = NoteAddForm(request.POST)
            if form.is_valid():
                req = form.save(commit=False)
                req.date = datetime.now()
                req.save()
        else:
            redirect('/')

        response = redirect('list')
        response['Location'] += '?qid={}'.format(request.POST.get('qid', 0))
        return response

    else:
        if request.GET.get('qid', '') == '':
            qid_found = Note.objects.all().aggregate(Max('qid'))
            qid_max = qid_found.get('qid__max')
            if qid_max is None:
                qid_max = 0
            else:
                qid_max += 1
            response = redirect('list')
            response['Location'] += '?qid={}'.format(qid_max)
            return response

        context = {
            'notes': [obj for obj in Note.objects.filter(qid=request.GET['qid'])],
            'qid': request.GET['qid']
        }
        return render(request, 'queue.html', context)
