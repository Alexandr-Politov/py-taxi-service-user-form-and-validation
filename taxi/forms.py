from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm

from taxi.models import Driver, Car


class DriverForm(UserCreationForm):
    license_number = forms.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{3}\d{5}$",
                message="For license number use 3 uppercase and 5 digits.",
            )
        ]
    )

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "license_number"
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{3}\d{5}$",
                message="For license number use 3 uppercase and 5 digits.",
            )
        ]
    )

    class Meta:
        model = Driver
        fields = ["license_number"]


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.prefetch_related("cars"),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Car
        fields = ("model", "manufacturer", "drivers")
