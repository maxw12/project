import datetime

from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import Submission


class CreateSubmissionForm(BSModalModelForm):
    """
    Form for the adding a topic to the system
    """
    title = forms.CharField(max_length=255)
    pub_date = forms.DateField(initial=datetime.date.today)
    url = forms.CharField(max_length=255)

    class Meta:
        model = Submission
        fields = ('title', 'pub_date', 'url', )