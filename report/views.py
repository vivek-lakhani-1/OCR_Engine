from django.shortcuts import render
from recognition_app.models import gujrati_files
def reportpage(request):
    gj = gujrati_files.objects.filter(email = request.session.get('key', None)).values()
    date = []
    name = []
    filename = []
    for i in range(len(gj)):
        date = gj[i]['time']
        name = gj[i]['email']
        image = gj[i]['image']
        
    
    prm = zip(date,name,image)
    
    print("---------------------------------------------------------")
    data = {
        'pr':prm
    }
    
    return render(request,'report.html',data)