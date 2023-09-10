from django.shortcuts import render
from django.views.generic import View

from main.utils import DataMixin



class main(DataMixin, View):
    def get(self, request, **kwargs):
        c_def = self.get_data()
        context = super().get_data(**kwargs)
        context['active_page'] = 'home'
        context = dict(list(context.items()) + list(c_def.items()))
        return render(request, 'main/main.html', context=context)


