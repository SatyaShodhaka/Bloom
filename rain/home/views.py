from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
# from accounts.models import UserProfile
from django.core.mail import send_mail
from .models import Feedback

# Create your views here.
def view_home(request):
#    form = PostForm()
#     posts = Post.objects.order_by('date').reverse()
#     args = {'form':form,'posts':posts} 
    return render(request,'base.html')

def feedback(request):
    if request.method == 'POST':
        sname = request.POST.get('name')
        smsg = request.POST.get('message')
        smail = request.POST.get('mail')
        sphone = request.POST.get('phone_no')
        p = Feedback(name=sname,message=smsg,mail = smail,phone_no = sphone)
        p.save()
        return redirect('')
    else:
        return render(request,'')