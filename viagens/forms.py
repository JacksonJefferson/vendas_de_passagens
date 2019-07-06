from django.forms import ModelForm
from . models import Passagem, Veiculo

class PassagemForm(ModelForm):
    class Meta:
        model = Passagem
        fields = '__all__'
    
class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'