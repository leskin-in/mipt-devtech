from django.db import models
from django.forms import ModelForm


class Note(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    qid = models.IntegerField(verbose_name='Note list ID', default=-1)
    header = models.CharField(verbose_name='Name', max_length=140)
    body = models.CharField(verbose_name='Contents', max_length=1024)
    date = models.DateTimeField(verbose_name='Creation date')

    def __str__(self):
        return str((self.qid, self.id, self.header, self.body, self.date))


class NoteAddForm(ModelForm):
    class Meta:
        model = Note
        fields = ['qid', 'header', 'body']
