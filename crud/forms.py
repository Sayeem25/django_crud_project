from django.forms import ModelForm
from .models import Info

class CreateInfo(ModelForm):
    class Meta:
        model = Info
        fields = '__all__'