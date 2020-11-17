# -*- coding: utf-8 -*-

from bottle import Bottle, response
import core
import json
import os

class srv:
    def __init__(self, host='', porta=8080):

        if os.environ.get('APP_LOCATION') == 'heroku':
           self._h = "0.0.0.0"
           self._p = int(os.environ.get("PORT", 5000))
        else:
           self._h = host
           self._p = porta

        self._a = Bottle()
        self._rota()
        self._g = core

    def _rota(self):
        self._a.route('/estacoes/', callback=self.getStations)
        self._a.route('/estacoes/<busca>', callback=self.getStations)

    def go(self):
        self._a.run(host=self._h, port=self._p)

    def getStations(self, busca=''):
        print
        response.headers['Access-Control-Allow-Origin']='*'
        response.headers['Content-Type']='application/json'
        _estacoes = self._g._get() if busca == '' else self._g._busca(busca)
        _bloco = []
        for _estacao in _estacoes:
            _nome, _lat, _long, _endereco, _linha, _statusOnline, _StatusOperacional, _disp1, _disp2, _total, _internalStatus, _img, _id = _estacao
            _bloco.append({ "type" : "Feature",
                            "geometry" : {
                                "coordinates": [ _long, _lat ],
                                "type": "Point" },
                            "properties": {
                                "id" : _id,
                                "nome" : _nome,
                                "endereco" : _endereco,
                                "estacao" : _linha,
                                "status_online": _statusOnline,
                                "status_operacional" : _StatusOperacional,
                                "qtd_bikes_disp_1" : _disp1,
                                "qtd_bikes_disp_2" : _disp2,
                                "qtd_vagas_total" : _total,
                                "statusInterno" : _internalStatus }
                         })
        return json.dumps({ "features" : _bloco, "type": "FeatureCollection" }, indent=2, sort_keys=True)

if __name__=='__main__':
    s=srv().go()
