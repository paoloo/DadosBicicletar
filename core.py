# -*- coding: utf-8 -*-

from selenium import webdriver

_page = webdriver.PhantomJS()

def _get():
    _page.get("http://www.bicicletar.com.br/mapaestacao.aspx")
    _estacoes = _page.execute_script("return beaches")
    return _estacoes

def _busca(criterio):
    _estacoes = _get()
    _bloco = []
    for _estacao in _estacoes:
        _nome, _lat, _long, _endereco, _linha, _statusOnline, _StatusOperacional, _disp1, _disp2, _total, _internalStatus, _img, _id = _estacao
        if ((criterio.decode('utf-8') in _nome) or (criterio.decode('utf-8') in _endereco) or (criterio.decode('utf-8') in _linha)):
            _bloco.append(_estacao)
    return _bloco