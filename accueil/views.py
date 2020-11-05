from django.shortcuts import render
from .forms import SearchForm
from .models import Communes
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

    return render(request, 'accueil/index.html', context)
