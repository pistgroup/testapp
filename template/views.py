from django.shortcuts import render,redirect
from .forms import DayCreateForm

def index(request):
    #トップページ
    context = {
        'name':'mitsuru',
    }
    return render(request,'template/index.html',context)

def add(request):
    #送信内容を元にフォームの作成。POSTじゃなければ空のフォーム
    form = DayCreateForm(request.POST or None)

    #入力内容が問題なければ / form.is_validで自動で判定しエラーメッセージを表示してくれる
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('template:index')

    #入力内容に誤りがあればまたページを表示
    contexts = {
        'form':form
    }
    return render(request,'template/about.html',contexts)

def info(request):
    # インフォ
   return render(request,'template/info.html')