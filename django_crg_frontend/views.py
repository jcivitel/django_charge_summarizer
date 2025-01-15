from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.utils.timezone import now


@login_required
def dashboard(request):
    template = loader.get_template("dashboard.html")
    template_opts = dict()

    template_opts["current_year"] = datetime.now().year
    template_opts["months"] = range(1, 13)
    template_opts["years"] = range(now().year - 5, now().year + 1)

    return HttpResponse(template.render(template_opts, request))
