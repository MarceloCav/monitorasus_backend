from django.urls import path
from .views import (
    MediaDiasInternacaoPorEspecialidade,
    NumeroPercentualInternacoesPorCausa,
    ValorMedioInternacaoPorEspecialidade,
    TaxaOcupacaoHospitalarPorEstabelecimento,
)

urlpatterns = [
    path('media-dias-internacao/', MediaDiasInternacaoPorEspecialidade.as_view(), name='media-dias-internacao'),
    path('numero-percentual-internacoes/', NumeroPercentualInternacoesPorCausa.as_view(), name='numero-percentual-internacoes'),
    path('valor-medio-internacao/', ValorMedioInternacaoPorEspecialidade.as_view(), name='valor-medio-internacao'),
    path('taxa-ocupacao/', TaxaOcupacaoHospitalarPorEstabelecimento.as_view(), name='taxa-ocupacao-hospitalar'),
]
