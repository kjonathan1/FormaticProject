from django.forms import ModelForm
from multiselectfield import MultiSelectFormField
from .models import *

class SessionForm(ModelForm):
    MY_CHOICES = (('item_key1', 'Item title 1.1'),('item_key2', 'Item title 1.2'),)
    class Meta:
        model = Session
        # module_ids = MultiSelectFormField(choices=MyModel.MY_CHOICES)
        fields = ['nom', 'start_date', 'description', 'module_ids']


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['nom', 'description']


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'


class InscriptionForm(ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'