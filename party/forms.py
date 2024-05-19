from django.forms import ModelForm, HiddenInput

from party.models import Submission


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = [
            'title',
            'sub_file',
            'thumbnail',
            'author',
            'description',
            'compo',
        ]
        widgets = {
            'compo': HiddenInput
        }