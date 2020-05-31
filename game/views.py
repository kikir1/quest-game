from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
    return redir(request, 1)

def game(request):

    ans = request.GET['option1']
    #quest = Questions.objects.get(quest=cur_quest)
    try:
        next_quest = Ans.objects.get(answer=ans).next_quest.id
        print(next_quest)
        return redirect(redir, next_quest)
    except:
        return render(request, "finish.html")

def redir(request, pk):
    quest = Questions.objects.get(id=pk)
    answer = Ans.objects.filter(quest=quest)

    return render(request, "quest.html", context={"quest": quest, 'answer': answer})
