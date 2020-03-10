from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'project_tracker'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('job_list', views.JobListView.as_view(), name='jobs_list'),
    path('open_items', views.OpenItemsView.as_view(), name='open_items'),
    path('project_schedule', views.ProjectScheduleView.as_view(), name='project_schedule'),
    path('inventory_control', views.InventoryControlView.as_view(), name='inventory_control'),
    path('wallcovering', views.WallcoveringView.as_view(), name='wallcovering'),
    path('go_to_job_finder', views.GoToJobFinderView.as_view(), name='go_to_job_finder'),
    path('book_new_job', views.BookNewJobView.as_view(), name='book_new_job')
]
