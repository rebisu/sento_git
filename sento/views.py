from django.shortcuts import render,redirect,get_object_or_404
from .forms import SentoDataForm
from django.http import HttpResponse
from .models import SentoData

def AddData(request):
    #送信内容をもとにフォームを作成する。POSTでなければからのフォーム
    form = SentoDataForm(request.POST or None)
    #method=POST、つまり送信ボタン押下時、入力内容に問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save() #insert文を内部的に発行する
        return redirect('sento:list')
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': SentoDataForm
    }
    return render(request,'sento/add.html',context)

def ListData(request):
    d = {
        'sentodata' : SentoData.objects.all(),
    }
    return render(request,'sento/list.html',d)

def Rank(request):
    return render(request,'sento/rank.html')

def Update(request, pk):
    #urlのpkをもとに、モデルを取得
    Sdata = get_object_or_404(SentoData, pk=pk)
    #formに取得したモデルを紐づける。
    form = SentoDataForm(request.POST or None, instance=Sdata)
    #method=POST、つまり送信ボタン押下時、入力内容に問題がなければ
    if request.method == 'POST' and form.is_vallid():
        form.save()
        return redirect('sento:list')

        #通常時のページアクセスや入力内容に誤りがあればまたページを表示
    context = {
        'form':form
    }
    return render(request,'sento/add.html',context)