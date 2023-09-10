from django.shortcuts import render
from django.views import View

from main.utils import DataMixin


def addgroups(request):
    return render(request, 'groups/groups.html')

class choice_game(DataMixin, View):
    def get(self, request, **kwargs):
        c_def = self.get_data()
        context = super().get_data(**kwargs)
        context['active_page'] = 'choice_game'
        context = dict(list(context.items()) + list(c_def.items()))
        return render(request, 'groups/game_modes.html', context=context)


