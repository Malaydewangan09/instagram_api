from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from instagram_private_api import Client, ClientCompatPatch



def home(request):       
    user_name = 'malay_2505'
    password = 'md@181120'
    api = Client(user_name, password)
    results = api.user_feed('6064500755')
    
    items = results.get('items', [])
    for item in items:
        ClientCompatPatch.media(item)
        print(media['code'])
    return render(reuest , 'index.html', {'data':items})

        
        
    
    




    
   
   

