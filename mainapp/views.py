from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'test.html')


def threshold(request):
    alert = False
    normal=False
    warning=False
    if (request.method=='POST'):
        hotspot = int(request.POST.get("hotspot"))
        high = int(request.POST.get('high'))
        batt = int(request.POST.get('batt', default="24"))
        offline =int(request.POST.get('offline', default="25"))
        current = int(request.POST.get('current', default="24"))

        if (batt<=hotspot and offline<=hotspot and current<= hotspot
            and batt<=high and offline<=high and current<= high):
            normal=True
        elif (batt>hotspot or offline>hotspot or current>hotspot):
            alert=True
        elif (batt>high or offline>high or current>high):
            warning=True            
        return render(request, 'test.html', {'Alert': alert,
                                         'Normal':normal,
                                         'Warning': warning})

    return render(request, 'temp.html')

