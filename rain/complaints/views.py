from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ComplaintForm
from .models import Complaint
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from accounts.models import UserProfile
from django.core.mail import send_mail

def view_complaint(request):
    posts = UserProfile.objects.all().filter(user_id = request.user.id)
    for e in posts:
        if e.is_admin == False:
            return render(request,'complaints/create.html')#mention not a staff member
        else:
            form = ComplaintForm()
            posts = Complaint.objects.all().order_by('date').filter(status = True)
            return render(request,'complaints/view.html',{'posts':posts})

@login_required
def reg_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit = False)
            p.status = True
            p.user = request.user
            posts = UserProfile.objects.all().filter(user_id = request.user.id)
            for e in posts:
                if e.is_admin == True:
                    return render(request,'complaints/create.html')
            else:
                p.save()
                return redirect('/')
        else:
            return render(request,'complaints/create.html')
    else:
        form = ComplaintForm()
        args = {'form':form}
        return render(request,'complaints/create.html/',args)

@login_required
def admin_complaint(request):
        form = ComplaintForm()
        posts = Complaint.objects.order_by('date')
        args = {'forms':form,'posts':posts}
        return render(request,'complaints/view.html',args)