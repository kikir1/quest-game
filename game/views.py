from datetime import time
from time import sleep

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
    return redir(request, 1)

def game(request):
    tittle = request.GET.get("tittle")
    print('sadfsdfascassdgffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',tittle)
    ans = request.GET.get("answer")
    print(ans)
    quest = Questions.objects.get(quest=tittle)
    print(quest)
    next_quest = Ans.objects.get(answer=ans, quest=quest).next_quest.id
    print("ddss", next_quest)
    if next_quest:
        return redirect(redir, int(next_quest))
    else:
        return render(request, "finish.html")


def redir(request, pk):
    quest = Questions.objects.get(id=pk)
    answer = Ans.objects.filter(quest=quest)

    return render(request, "quest.html", context={"quest": quest, 'answer': answer})
