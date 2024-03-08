from django.urls import path
from .views import InteresadoListCreateView, BachilleratoListCreateView, LicenciaturaListCreateView, GradoAcademicoListCreateView, VisitaListCreateView

urlpatterns = [
    path('interesados/', InteresadoListCreateView.as_view(), name='interesado-list-create'),
    path('bachilleratos/', BachilleratoListCreateView.as_view(), name='bachillerato-list-create'),
    path('licenciaturas/', LicenciaturaListCreateView.as_view(), name='licenciatura-list-create'),
    path('grados-academicos/', GradoAcademicoListCreateView.as_view(), name='grado-academico-list-create'),
    path('visitas/', VisitaListCreateView.as_view(), name='visita-list-create'),
]