from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'คุณลงทะเบียนเรียบร้อยแล้ว, สามารถใช้งานได้ทันที')
            return redirect('login')
    else:
        form = UserCreationForm()

    context = { 'form' : form }
    return render(request, 'users/register.html', context)
