from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redir(request, 1)

def game(request):
    cur_quest = request.GET.get("tittle")
    ans = request.GET.get("answer")
    quest = Questions.objects.get(quest=cur_quest)
    try:
        next_quest = Ans.objects.get(answer=ans, quest=quest).next_quest.id
        return HttpResponse("/" + str(next_quest))
    except:
        return render(request, "finish.html")


def redir(request, pk):
    quest = Questions.objects.get(id=pk)
    answer = Ans.objects.filter(quest=quest)

    return render(request, "quest.html", context={"quest": quest, 'answer': answer})
