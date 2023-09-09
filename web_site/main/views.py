from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')

def choice_game(request):
    return render(request, 'main/choice_game.html')