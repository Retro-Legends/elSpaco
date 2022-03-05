from django.forms import ModelForm
from .models import Cladire


class CladireForm(ModelForm):
    class Meta:
        model = Cladire
        fields = '__all__'
