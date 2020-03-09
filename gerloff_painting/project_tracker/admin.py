from django.contrib import admin
from .models import *
gerloff_Painting_Models = [Change_Orders, Checklist, Clients, Estimates, Extra_Work_Tickets, Incoming_Wall_Covering, Inventory_Type, Storage_Location_Type, Inventory, Jobs, TM_Prices, TM_List, Client_Information, Orders, Outgoing_Wallcovering, Packages, Plans, Subcontractors, Submittal_Items, Submittals, Wallcovering]  # iterable list
admin.site.register(gerloff_Painting_Models)
# Register your models here.
