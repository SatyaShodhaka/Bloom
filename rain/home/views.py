from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
# from accounts.models import UserProfile
from django.core.mail import send_mail
from .models import Feedback
from .forms import FeedbackForm

# Create your views here.
def view_home(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit = False)
            p.user = request.user
            p.save()
        return redirect('/')
    else:
        return render(request,'base.html')
