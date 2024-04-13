from django.shortcuts import render
from .models import Client, Sale

# Create your views here.
def index(request):
    return render(request, 'intro.html')

def clients(request):
    return render(request, 'clients.html', {
        'clients': Client.objects.all()
    })

def sales(request):
    return render(request, 'sales.html', {
        'sales': Sale.objects.all()
    })

def report(request):
    if request.method == 'POST':
        filter_first_date = request.POST.get('first_date')
        filter_last_date = request.POST.get('last_date')

        sales = Sale.objects.filter(creatin_date__range=[filter_first_date, filter_last_date])
        if not sales:
            return render(request, 'report.html', {
                'error': 'No sales found in the given date range.'
            })
        
        print(sales)

        return render(request, 'report.html', {
            'sales': sales
        })
    else:
        return render(request, 'report.html')
