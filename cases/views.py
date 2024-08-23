from django.shortcuts import render 
# Create your views here.

def index(request):    
    
    context = {  
              }
    return render(request, 'index.html', context)

def main(request):    
    
    context = {            
    }
    return render(request, 'admin/main.html', context)

def client(request):    
    
    context = {            
    }
    return render(request, 'client/client.html', context)

def all_clients(request):    
    all_clients = [
        
            { "client_id": '01', "client_name": "سميرعادل سمير", "num_cases": "2" , "nationality":'الاردنية', "address": 'حبل الحسين', "contact": '0781111111' },
            { "client_id": '02', "client_name": "مروان عادل مروان", "num_cases": "1" , "nationality":'الاردنية',  "address": 'صويلح',  "contact": '0782222222'},
            { "client_id": '03', "client_name": "عبدالله عادل عبدالله", "num_cases": "1" , "nationality":'الاردنية',  "address": 'الصويفية', "contact": '0783333333' },
            { "client_id": '04', "client_name": "علي عادل علي", "num_cases": "1" , "nationality":'الاردنية',  "address": 'المدينة الرياضية', "contact": '0784444444'},
            { "client_id": '05', "client_name": "كمال عادل كمال", "num_cases": "0"  , "nationality":'الاردنية',  "address": 'عين الباشا', "contact": '0785555555'},
            { "client_id": '06', "client_name": "جمال عادل جمال", "num_cases": "0", "nationality":'الاردنية',  "address": 'خلدا', "contact": '0786666666'},
            { "client_id": '07', "client_name": "اياد عادل اياد", "num_cases": "0" , "nationality":'الاردنية',  "address": 'وادي السير', "contact": '0787777777'},
            { "client_id": '08', "client_name": "سوسن عادل عادل", "num_cases": "0" , "nationality":'الاردنية',  "address": 'طبربور', "contact": '0788888888'},
    ]
    context = {        
               "all_clients":all_clients,
    }
    return render(request, 'admin/all_clients.html', context)


def all_lawyers(request):        
    all_lawyers = [
        
            { "lawyer_id": '01', "lawyer_name": "محامي مكتب رقم 1", "num_cases": "3"  , "address": 'حبل الحسين', "contact": '0781111111' },
            { "lawyer_id": '02', "lawyer_name": "محامي مكتب رقم 2", "num_cases": "1"  ,  "address": 'صويلح',  "contact": '0782222222'},
            { "lawyer_id": '03', "lawyer_name": "محامي مكتب رقم 3", "num_cases": "1"  ,  "address": 'الصويفية', "contact": '0783333333' },
            
    ]
    context = {        
               "all_lawyers":all_lawyers,
    }
    return render(request, 'admin/all_lawyers.html', context)


def client_cases(request): 
    clients = [
        
            { "client_name": "سميرعادل سمير", "client_tradeno": "لا يوجد" , "client_nationality":'الاردنية', "full_address": 'حبل الحسين', "contact": '0781111111', "email":"clients@gmail.com" },
          ]   
    client_cases = [
        
            { "case_id": 'case_01', "client_type": "مدعي", "case_lawyer": "محامي مكتب رقم 1"  , "opp_lawyer": 'محامي خصم رقم 1', "opp_contact": '0781111111', "amm1":"4600.00","amm2":"3800.00","amm3":"800.00" },
            { "case_id": 'case_02', "client_type": "مدعى عليه", "case_lawyer": "محامي مكتب رقم 1"  ,  "opp_lawyer": 'محامي خصم رقم 2',  "opp_contact": '0782222222', "amm1":"2500.00","amm2":"0.00","amm3":"2500.00"},
            
            
    ]
    context = {        
               "client_cases":client_cases,
               "clients":clients,
    }
    return render(request, 'admin/client_cases.html', context)


def all_cases(request): 
   
    client_cases = [
        
            { "case_id": 'case_01', "client_name": "سميرعادل سمير", "contact": '0781111111', "client_type": "مدعي", "case_lawyer": "محامي مكتب رقم 1" , "amm1":"4600.00","amm2":"3800.00","amm3":"800.00" },
            { "case_id": 'case_02', "client_name": "سميرعادل سمير",  "contact": '0781111111', "client_type": "مدعى عليه", "case_lawyer": "محامي مكتب رقم 1"  , "amm1":"2500.00","amm2":"0.00","amm3":"2500.00"},
            { "case_id": 'case_03', "client_name": "مروان عادل مروان",  "contact": '0782222222', "client_type": "مدعي", "case_lawyer": "محامي مكتب رقم 1"  , "amm1":"1400.00","amm2":"0.00","amm3":"1400.00"},
            { "case_id": 'case_04', "client_name": "عبدالله عادل عبدالله",  "contact": '0783333333', "client_type": "مدعى عليه", "case_lawyer": "محامي مكتب رقم 2"  , "amm1":"6200.00","amm2":"0.00","amm3":"6200.00"},
            { "case_id": 'case_05', "client_name": "علي عادل علي",  "contact": '0784444444', "client_type": "مدعي", "case_lawyer": "محامي مكتب رقم 3"  , "amm1":"3200.00","amm2":"0.00","amm3":"3200.00"},
            
    ]
    context = {        
               "client_cases":client_cases,
                
    }
    return render(request, 'admin/all_cases.html', context)


def lawyer_cases(request): 
    lawyers = [
        {"name":"محامي مكتب رقم 1", "address":"حبل الحسين", "email":"lawyer1@gmail.com", "contact":"0781111111", "special":"قضايا مدنية", "regno":"121212",  }
    ]
   
    lawyer_cases = [
        
            { "case_id": 'case_01', "client_name": "سميرعادل سمير", "contact": '0781111111', "client_type": "مدعي", "case_lawyer": "محامي مكتب رقم 1" , "amm1":"4600.00","amm2":"3800.00","amm3":"800.00" },
            { "case_id": 'case_02', "client_name": "سميرعادل سمير",  "contact": '0781111111', "client_type": "مدعى عليه", "case_lawyer": "محامي مكتب رقم 1"  , "amm1":"2500.00","amm2":"1000.00","amm3":"1500.00"},
            { "case_id": 'case_03', "client_name": "مروان عادل مروان",  "contact": '0782222222', "client_type": "مدعي", "case_lawyer": "محامي مكتب رقم 1"  , "amm1":"1400.00","amm2":"1400.00","amm3":"0.00"},
          
            
    ]
    context = {        
               "lawyer_cases":lawyer_cases,
               "lawyers":lawyers,
                
    }
    return render(request, 'admin/lawyer_cases.html', context)


def pay_details1(request):
    
    payments = [
         {"amount": '2000.00' , "description" : "دفعة مالية ثالثة من اتعاب القضية "}
    ]
    
    context = {                     
       "payments":payments,
       "clients_name": "سمير عادل سمير",
    }
    
    return render(request, 'admin/pay_details1.html', context)


def pay_details2(request):
    expenses = [
         {"amount": '50.00' , "description" : "شراء قرطاسية ومستلزمات للمكتب", "person_name": "المكتبة العامة للقرطاسية"}
    ]
    
    context = {                     
         "expenses":expenses,
           
    }
    
    return render(request, 'admin/pay_details2.html', context)


def full_payments(request):
    payments = [
        
        {"payment_date":"12-07-2024", "receipt_id":"100", "amount":"2000.00", "case_id":"01", "description":"دفعة مالية ثالثة من اتعاب القضية"}         
    ]
    context = {                   
         "payments":payments,
    }    
    return render(request, 'admin/full_payments.html', context)

def full_expenses(request):
    expenses = [
        
        {"expenses_date":"12-07-2024", "receipt_id":"177", "amount":"50.00", "case_id":"01", "description":"شراء قرطاسية ومستلزمات للمكتب"}         
    ]
    
    context = {                   
         "expenses":expenses,
    }    
    return render(request, 'admin/full_expenses.html', context)    


def case_details(request):
    context = {                                   
          
    }    
    return render(request, 'admin/case_details.html', context)    




def sys_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        if user_name == "admin" and password == "admin":
           context = {                                   
          
           }       
           return render(request, 'admin/main.html', context)   
        if user_name == "client" and password == "client":
            context = {                                   
          
            }       
            return render(request, 'clients/client.html', context)       
        
    context = {                                   
          
    }    
    return render(request, 'guest/sys_login.html', context)    
    

def add_client(request):    
    
    context = {  
              }
    return render(request, 'admin/add_client.html', context)

def add_lawyer(request):    
    
    context = {  
              }
    return render(request, 'admin/add_lawyer.html', context)


def add_case(request):    
    
    context = {  
              }
    return render(request, 'admin/add_case.html', context)
