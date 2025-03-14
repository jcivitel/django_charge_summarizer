import os
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from django_crg_frontend.forms import UploadFileForm


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"WELCOME {user}")
            return redirect("dashboard")
        else:
            messages.error(request, _("Invalid username or password"))
    return render(request, "login.html")


@login_required
def dashboard(request):
    template = loader.get_template("dashboard.html")
    template_opts = dict()

    template_opts["current_year"] = datetime.now().year
    template_opts["months"] = range(1, 13)
    template_opts["years"] = range(now().year - 5, now().year + 1)

    return HttpResponse(template.render(template_opts, request))


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, _("You have been logged out 🫡"))
    return redirect("login")


@login_required
def upload_view(request):
    template = loader.get_template("upload_invoice.html")
    template_opts = dict()
    upload_path = os.path.join(settings.MEDIA_ROOT, "upload")

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist("files")
            for uploaded_file in files:
                with open(f"{upload_path}/{uploaded_file.name}", "wb+") as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
            messages.success(request, _("Files uploaded successfully. The files will be processed in the background"))
            return redirect("dashboard")
        else:
            messages.error(request, _("Only .zip or .pdf files are allowed"))
            return redirect("upload_invoice")
    else:
        form = UploadFileForm()
        template_opts["form"] = form

    return HttpResponse(template.render(template_opts, request))
