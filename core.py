# -*- coding: utf-8 -*-

import requests, re, json

_transtable = (
    (u'ã', u'a'), (u'â', u'a'), (u'ä', u'a'), (u'á', u'a'), (u'à', u'a'),
    (u'é', u'e'), (u'è', u'e'), (u'ê', u'e'), (u'ẽ', u'e'), (u'ë', u'e'),
    (u'í', u'i'), (u'ì', u'i'), (u'î', u'i'), (u'ï', u'i'), (u'ĩ', u'i'),
    (u'ó', u'o'), (u'ò', u'o'), (u'ô', u'o'), (u'õ', u'o'), (u'ö', u'o'),
    (u'ú', u'u'), (u'ù', u'u'), (u'û', u'u'), (u'ũ', u'u'), (u'ü', u'u'),
    (u'ç', u'c'),
    )

def _limpa(texto):
    _output = texto.lower()
    for _o, _d in _transtable:
        _output = _output.replace(_o, _d)
    return _output

def _get():
    dados = requests.get("http://www.bicicletar.com.br/mapaestacao.aspx")
    conteudo = dados.text
    estacoes = re.search("beaches = (.*)\>", conteudo).group()[10:][:-6].replace('"','').replace("'",'"')
    estacoes = estacoes[:-2] + estacoes[-1:]
    _estacoes = json.loads(estacoes)
    return _estacoes

def _busca(criterio):
    _criterio = criterio.lower()
    _criterio = _limpa(_criterio)
    _estacoes = _get()
    _bloco = []
    for _estacao in _estacoes:
        _nome, _lat, _long, _endereco, _linha, _statusOnline, _StatusOperacional, _disp1, _disp2, _total, _internalStatus, _img, _id = _estacao
        if ((_criterio in _limpa(_nome)) or (_criterio in _limpa(_endereco)) or (_criterio in _limpa(_linha))):
            _bloco.append(_estacao)
    return _bloco
