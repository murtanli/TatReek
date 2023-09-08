from django.shortcuts import render

def addgroups(request):
    return render(request, 'groups/groups.html')
