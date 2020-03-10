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
    def get_queryset(self):
        return;

class JobListView(generic.ListView):
    template_name = 'project_tracker/job_list.html'
    context_object_name = 'jobs'
    def get_queryset(self):
        return Jobs.objects.all().order_by('-booked_date')[0:2000]

class OpenItemsView(generic.ListView):
    template_name = 'project_tracker/open_items.html'
    def get_queryset(self):
        return;

class ProjectScheduleView(generic.ListView):
    template_name = 'project_tracker/project_schedule.html'
    def get_queryset(self):
        return;

class InventoryControlView(generic.ListView):
    template_name = 'project_tracker/inventory_control.html'
    def get_queryset(self):
        return;

class WallcoveringView(generic.ListView):
    template_name = 'project_tracker/wallcovering.html'
    def get_queryset(self):
        return;

class GoToJobFinderView(generic.ListView):
    template_name = 'project_tracker/go_to_job_finder.html'
    def get_queryset(self):
        return;

class BookNewJobView(generic.ListView):
    template_name = 'project_tracker/book_new_job.html'
    def get_queryset(self):
        return;
