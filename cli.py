# -*- coding: utf-8 -*-

import core
import sys

if __name__ == "__main__":
    _estacoes = core._busca(sys.argv[1]) if len(sys.argv) > 1 else core._get()
    i=0
    print "PROJETO BICICLETAR - FORTALEZA/BR"
    for _estacao in _estacoes:
        _nome, _lat, _long, _endereco, _linha, _statusOnline, _StatusOperacional, _disp1, _disp2, _total, _internalStatus, _img, _id = _estacao
        print 'estacao id %d:' % _id, _nome, '-', _linha, '-', _endereco, ' / bikes disponiveis: %d, vagas livres: %d' % (int(_disp2),int(_total))
        i+=1
    print 'foram mostradas %d estacoes' % i
 