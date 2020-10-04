from django.urls import path
from .views import HistoriaView2, RecetasPacientes, NuevaRecetaPacientes, DetalleRecetaPacientes, DetalleRecetas, TomaSignosPacientes
app_name = "atencion"
urlpatterns = [
    path('historia/', HistoriaView2.as_view(), name='historia'),
    path('recetas/', RecetasPacientes.as_view(), name='recetas'),
    path('nuevaReceta/', NuevaRecetaPacientes.as_view(), name='nuevaReceta'),
    path('detalleReceta/',DetalleRecetaPacientes.as_view(), name='detalle'),
    path('detalleRecetaP/',DetalleRecetas.as_view(), name='d'),
    path('tomaSigno/',TomaSignosPacientes.as_view(), name='toma')
]
