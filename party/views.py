from django.views.generic.detail import DetailView

from party.models import Compo, Party


class PartyDetailView(DetailView):
    model = Party 
    template_name = 'party/compo_detail.html'