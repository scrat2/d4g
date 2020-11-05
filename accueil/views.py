from django.shortcuts import render
from .forms import SearchForm
from .models import Communes, Departements
# Create your views here.


def index(request):
    form = SearchForm
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)

        if form.is_valid():
            postalcode = form.cleaned_data['postalCode']
            # region = form.cleaned_data['region']
            # departement = form.cleaned_data['departement']
            # commune = form.cleaned_data['commune']

            results = None

            if postalcode != "":
                results = Communes.objects.filter(code_postal=postalcode)

         #  if departement != "":
             #import re
            # results = Communes.objects.filter(re.search(r'^Departements.numdep[0-9]{3}', Communes.code_postal))

    return render(request, 'accueil/index.html', context)

def listdep(request):
    departements = Departements.objects.filter(available=True)
    formatted_dep = ["<li>{}</li>".format(Departements.libdep) for Departements in departements]
    message = """<ul>{}</ul>""".format("\n".join(formatted_dep))
    return HttpResponse(message)
