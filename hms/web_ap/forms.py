from django import forms

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from web_ap.models import Participant

class NewParticipantForm(forms.Form):
    # Name fields could be expanded in real app

    max_name_length=20
    last_name=forms.CharField(widget=forms.TextInput,label='Last Name',
    max_length=max_name_length,required=True)

    first_name=forms.CharField(widget=forms.TextInput,label='First Name',
    max_length=max_name_length,required=True)

    SIB_CHOICES=(('Y','YES'),('N','NO'))
    siblings=forms.CharField(widget=forms.RadioSelect(
    choices=SIB_CHOICES),)

    EXPOSURE_CHOICES = (('PB', 'Pb'),('SS', 'Secondhand Smoke'),("NA",'Not applicable'),)
    environmental_exposures = forms.CharField(widget=forms.RadioSelect(
    choices=EXPOSURE_CHOICES),)

    MUTATION_CHOICES = (('MM', 'Missense mutation'),
        ('NM', 'Nonsense mutation'),('NA','Not applicable'),)
    genetic_mutations = forms.CharField(widget=forms.RadioSelect(
    choices=MUTATION_CHOICES),)
