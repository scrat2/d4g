from django.shortcuts import render
from .forms import SearchForm
from .models import Communes, Departements, Regions


# Create your views here.


def index(request):

    # Set bases of the view
    form = SearchForm
    regions = Regions.objects.all()
    context = {
        'form': form,
        'regions': regions
    }

    if request.method == 'POST':

        form = SearchForm(request.POST, request.FILES)

        if form.is_valid():

            # Get forms data
            libreg = request.POST.get('regions')
            libdep = request.POST.get('departements')
            libcom = request.POST.get('communes')
            postalcode = form.cleaned_data['postalCode']

            # Check postal code to see if it has been filled
            if postalcode != "":
                # Get communes with this postal code in the database
                communes = Communes.objects.filter(code_postal=postalcode)

                # Send all communes in the HTML
                context['communes'] = communes

            # Check region to see if it has been filled
            if libreg != "":
                # Get region with this name in the database
                region = Regions.objects.get(libreg=libreg)

                # Get departements in this region in the database
                departements = Departements.objects.filter(numreg_id=region.numreg)

                # Send all departements in the HTML
                context['departements'] = departements

                # Set the region selected in the session to maintain it in the form
                request.session['libreg'] = libreg
                context['default_libreg'] = request.session['libreg']

                # Check departement to see if it has been filled
                if libdep != "":
                    # Get departement with this name in the database
                    departement = Departements.objects.get(libdep=libdep)

                    # Get communes in this region in the database
                    communes = Communes.objects.filter(numdep=departement.numdep)

                    # Send all communes in the HTML
                    context['communes'] = communes

                    # Set the departement selected in the session to maintain it in the form
                    request.session['libdep'] = libdep
                    context['default_libdep'] = request.session['libdep']

                    # Check commune to see if it has been filled
                    if libcom != "":
                        # Get communes with this name in this departement in the database
                        communes = Communes.objects.filter(libcom=libcom, numdep=departement.numdep)
                        final_list = []
                        if request.session.get('final', None):
                            for liste in request.session['final']:
                                final_list.append(liste)

                        for commune in communes:
                            tmp = [region.libreg, region.global_score, region.numeric_access, region.information_access, region.numeric_competence, region.administrative_competence,
                                   departement.libdep, departement.global_score, departement.numeric_access, departement.information_access, departement.numeric_competence, departement.administrative_competence,
                                    commune.libcom, commune.global_score, commune.numeric_access, commune.information_access, commune.numeric_competence, commune.administrative_competence]
                            final_list.append(tmp)

                        request.session['final'] = final_list
                        # Send all communes in the HTML
    if request.session.get('final', None):
        context['final'] = request.session['final']

    return render(request, 'accueil/index.html', context)
