# -*- coding: utf-8 -*-

from bottle import Bottle, response
import core
import json

class srv:
    def __init__(self, host='', porta=8080):
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
                                "name" : _nome,
                                "address" : _endereco,
                                "station" : _linha,
                                "onlineStatus": _statusOnline,
                                "operationaStatus" : _StatusOperacional,
                                "bikesAvailable" : _disp1,
                                "bikesAvailable2" : _disp2,
                                "totalVacancies" : _total,
                                "internalStatus" : _internalStatus }
                         })
        return json.dumps({ "features" : _bloco, "type": "FeatureCollection" })

if __name__=='__main__':
    s=srv().go()
