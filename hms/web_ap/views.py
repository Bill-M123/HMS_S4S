from django.shortcuts import render

# Create your views here.

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from web_ap.models import Participant
from web_ap.forms import NewParticipantForm


@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_participants = Participant.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_participants': num_participants,
        'num_visits': num_visits,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class All_Participants_ListView(LoginRequiredMixin,generic.ListView):
    model = Participant

@login_required
def new_participant(request):
    """View function for testing a new target/reference pair."""

    new_participant = Participant()

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = NewParticipantForm(request.POST)
        print(form)
        if form.is_valid():
            #
            new_participant.first_name=form.cleaned_data['first_name']
            #print(new_participant.first_name)
            new_participant.last_name=form.cleaned_data['last_name']
            new_participant.siblings=form.cleaned_data['siblings']
            new_participant.environmental_exposures=form.cleaned_data['environmental_exposures']
            new_participant.genetic_mutations=form.cleaned_data['genetic_mutations']

            new_participant.save()

            # redirect to show all resulting pairs:
            participant_list=Participant.objects.all()
            context={'participant_list':participant_list}#prep_results(target_reference_pair)
            return render(request, 'results.html', context)
        else:
            context={'form':form}
            return HttpResponse('Problem with new participant.  Try again.')
    else:
        form = NewParticipantForm()
        context={'form':form}
        return render(request, 'web_ap/new_participant.html', context)
