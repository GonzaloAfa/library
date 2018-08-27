from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from record.models import Record
from system_auth.models import Workspace


@login_required(login_url='/')
def index(request):

    ref_workspace= Workspace.objects.filter(ref_profile=request.user.profile, active=True).first()
    total_records = Record.objects.filter(ref_workspace =ref_workspace ).count()

    # print({'records': records})

    return render(request, 'home/index.html', {'total_records': total_records} )
