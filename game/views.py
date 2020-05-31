from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Questions, Answ

# Create your views here.


def index(request):

    quest = Questions.objects.get(id=1)
    answer = Answ.objects.filter(quest=1)

    return render(request, "index.html", context={"quest": quest, 'answer': answer})

def game(request):

    cur_quest = request.GET['tittle']
    ans = request.GET['answer']
    quest = Questions.objects.get(quest=cur_quest)
    next_quest = Answ.objects.get(answer=ans, quest=quest).nq
    answers = Answ.objects.filter(quest=next_quest)
    answer = []
    for ans in answers:
        a = ans.answer
        answer.append(a)

    response = {
        "quest": next_quest.quest,
        "answer": answer
    }

    return redirect("game")

def redir(request):
    print("hf,jnftn")
    redirect("/1/")

def test(request, pk):
    quest = Questions.objects.get(id=pk)
    answer = Answ.objects.filter(quest=quest)

    return render(request, "quest.html", context={"quest": quest, 'answer': answer})
