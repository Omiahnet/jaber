from django.urls import path
from cases import views
 


app_name = 'cases'

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('client', views.client, name='client'),
    
    path('all_clients', views.all_clients, name='all_clients'),   
    path('add_client', views.add_client, name='add_client'),
    
    path('all_lawyers', views.all_lawyers, name='all_lawyers'), 
    path('add_lawyer', views.add_lawyer, name='add_lawyer'),
    path('add_case', views.add_case, name='add_case'),
      
    path('client_cases', views.client_cases, name='client_cases'),   
    
    path('all_cases', views.all_cases, name='all_cases'),  
    path('lawyer_cases', views.lawyer_cases, name='lawyer_cases'),  
    path('pay_details1', views.pay_details1, name='pay_details1'),
    path('pay_details2', views.pay_details2, name='pay_details2'),
    
    
    path('full_payments', views.full_payments, name='full_payments'),
    path('full_expenses', views.full_expenses, name='full_expenses'),
    path('case_details', views.case_details, name='case_details'),
    
    path('sys_login', views.sys_login, name='sys_login'),
    
    
    
    
   
]