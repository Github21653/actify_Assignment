from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/' + ip_data['ip'])
    loc_data = res.text
    data = json.loads(loc_data)
    return render(request, 'index.html', {'data': data})