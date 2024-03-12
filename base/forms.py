from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Jugador
class CustomUserCreationForm(UserCreationForm):
    pass



class JudadorForm(ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre_jugador', 'apellido_jugador', 'foto','fecha_nacimiento','posicion','equipo','numero_camiseta','titular']