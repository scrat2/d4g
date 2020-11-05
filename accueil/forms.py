from django import forms


class SearchForm(forms.Form):

    postalCode = forms.CharField(
        label='PostalCode',
        widget=forms.NumberInput(attrs={'placeholder': 'Code postal'}),
        max_length=5,
        required=False
    )

    region = forms.CharField(
        label='region',
        widget=forms.TextInput(attrs={'placeholder': 'Region'}),
        max_length=50,
        required=False
    )

    departement = forms.CharField(
        label='departement',
        widget=forms.TextInput(attrs={'placeholder': 'Departement'}),
        max_length=50,
        required=False
    )

    commune = forms.CharField(
        label='commune',
        widget=forms.TextInput(attrs={'placeholder': 'Commune'}),
        max_length=50,
        required=False
    )