from django.shortcuts import render
from django.http import HttpResponse
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import os, sys, django
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views import generic
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Jobs
#from django.contrib.auth import logout as auth_logout, login
#from .current_jobs import Current_Jobs
#from django.contrib.auth.decorators import login_required, permission_required
#from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
django.setup()

class IndexView(generic.ListView):
    template_name = 'project_tracker/index.html'
    context_object_name = 'jobs'
    def get_queryset(self):
        return Jobs.objects.all().order_by('-booked_date')[0:2000]
