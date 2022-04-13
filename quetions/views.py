from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Answers,Quetions

def home(request):
    return render(request,'quetions/home.html')

@csrf_exempt
def get_answer(request):
    if request.method == 'POST':
        que = request.POST.get('q')
        d = Quetions.objects.filter(quetion__icontains = que).first()
        ans = Answers.objects.filter(quetion = d.id).first()
        print(ans,"ans")
        k = ans.answer.split(".")
        print(k)
        return render(request,'quetions/home.html',{"ans":k,"q":d.quetion})
    else:
        d = Quetions.objects.all()
        print(d)
        return render(request,'quetions/home.html',{"q":d})


@csrf_exempt
def get_answer2(request,n):
    d = Quetions.objects.filter(id = n).first()
    ans = Answers.objects.filter(quetion = d.id).first()
    print(ans,"ans")
    k = ans.answer.split(".")
    print(k)
    return render(request,'quetions/home2.html',{"ans":k,"q":d.quetion})