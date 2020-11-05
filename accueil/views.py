from django.shortcuts import render
from .forms import SearchForm
from .models import Communes, Departements, Regions


# Create your views here.


def index(request):
    form = SearchForm
    regions = Regions.objects.all()
    context = {
        'form': form,
        'regions': regions
    }

    if request.method == 'POST':
        libreg = request.POST.get('regions')
        libdep = request.POST.get('departements')
        libcom = request.POST.get('communes')
        form = SearchForm(request.POST, request.FILES)
        results = None
        if form.is_valid():
            postalcode = form.cleaned_data['postalCode']

            print(postalcode)

            if postalcode != "":
                communes = Communes.objects.filter(code_postal=postalcode)
                context['communes'] = communes

            if libreg != "":
                region = Regions.objects.get(libreg=libreg)
                departements = Departements.objects.filter(numreg_id=region.numreg)
                context['departements'] = departements

            if libdep != "":
                departement = Departements.objects.get(libdep=libdep)
                communes = Communes.objects.filter(numdep=departement.numdep)
                context['communes'] = communes

            if libcom != "":
                results = Communes.objects.filter(libcom=libcom)
                context['resultats'] = results

    return render(request, 'accueil/index.html', context)
