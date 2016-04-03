# DadosBicicletar
### Status das estações do projeto bicicletar, de Fortaleza/BR, como API e aplicacao

Trata-se de um extrator de dados do do bicicletar, atraves dos scripts em seu site,
fornecendo esta informação tanto diretamente no terminal, quanto como uma API,
retornando um **GeoJSON** (especificação e documentação do GeoJSON:
http://geojson.org/geojson-spec.html) do status em tempo real das estações. Um exemplo
do **GeoJSON** gerado pode ser visto no arquivo [estacoes.geojson](estacoes.geojson).
As informações são tratadas de forma a propiciar tanto uma visão completa de todas as
estações quanto apenas informações resultantes de uma busca de estações por local.

A ideia, ao desenvolver isto, foi propiciar a criação de hooks que chequem os dados
regularmente e informem quando houver uma bike disponivel em uma estacao especifica,
bem como procurar estações em uma região especifica para depositar a bike,
planejando o deslocamento de forma mais eficiente.

### Requisitos
- python 2.7
- bottle ( bottlepy.org - mas ja vai embarcado)
- selenium
- PhantomJS

### Uso - modo API

- diretamente no terminal:
```
python api.py
```
- ou, em modo *deamon*:
```
nohup python web.py &
```

#### Requisição
```
http://localhost:8080/estacoes
```
para buscar estações que tenham certo critério
```
http://localhost:8080/estacoes/k
```
onde **k** é a rua ou nome da estação que se procura.

### Uso - modo terminal
```
python cli.py [criterio de busca]
```
onde o criterio de busca, se informado, trará, apenas, as estações que se
adequarem ao criterio definido


### Exemplo da saida da API da busca por "Bezerra" com a URL: http://localhost:8080/estacoes/Bezerra
```
{
	"type": "FeatureCollection",
	"features": [{
		"geometry": {
			"type": "Point",
			"coordinates": [-38.547983, -3.732094]
		},
		"type": "Feature",
		"properties": {
			"qtd_bikes_disp_1": "8",
			"statusInterno": "Est_Normal 1",
			"status_operacional": "EO",
			"qtd_vagas_total": "4",
			"nome": "Parque Arax&#225;",
			"endereco": "Avenida Bezerra de Menezes, 334 / Esquina Rua Ribeiro da Silva",
			"qtd_bikes_disp_2": "8",
			"estacao": "Parque Arax&#225;",
			"id": 37,
			"status_online": "A"
		}
	}, {
		"geometry": {
			"type": "Point",
			"coordinates": [-38.551978, -3.7331071]
		},
		"type": "Feature",
		"properties": {
			"qtd_bikes_disp_1": "9",
			"statusInterno": "Est_Normal 1",
			"status_operacional": "EO",
			"qtd_vagas_total": "3",
			"nome": "Instituto dos Cegos",
			"endereco": "Canteiro Central da Avenida Bezerra de Menezes, 801 / Esquina Rua Padre Anchieta",
			"qtd_bikes_disp_2": "9",
			"estacao": "Instituto dos Cegos",
			"id": 38,
			"status_online": "A"
		}
	}, {
		"geometry": {
			"type": "Point",
			"coordinates": [-38.563427, -3.7354169]
		},
		"type": "Feature",
		"properties": {
			"qtd_bikes_disp_1": "11",
			"statusInterno": "Est_Normal 1",
			"status_operacional": "EO",
			"qtd_vagas_total": "1",
			"nome": "&#201;rico Mota",
			"endereco": "Avenida Bezerra de Menezes, 2080 / Esquina Rua Eduardo Barros Leal",
			"qtd_bikes_disp_2": "11",
			"estacao": "Esquina com a Rua Eduardo Barros Leal",
			"id": 41,
			"status_online": "A"
		}
	}, {
		"geometry": {
			"type": "Point",
			"coordinates": [-38.565929, -3.7357836]
		},
		"type": "Feature",
		"properties": {
			"qtd_bikes_disp_1": "4",
			"statusInterno": "Est_Normal 1",
			"status_operacional": "EO",
			"qtd_vagas_total": "8",
			"nome": "North Shopping",
			"endereco": "Avenida Bezerra de Menezes, 2500",
			"qtd_bikes_disp_2": "4",
			"estacao": "North Shopping",
			"id": 42,
			"status_online": "A"
		}
	}]
}
```
### Exemplo da saida do terminal com a busca por estacoes na "Bezerra"
```
paolo@abyss:~/Sources/DadosBicicletar$ python cli.py Bezerra
PROJETO BICICLETAR - FORTALEZA/BR
estacao id 37: Parque Araxá - Parque Araxá - Avenida Bezerra de Menezes, 334 / Esquina Rua Ribeiro da Silva / bikes disponiveis: 8, vagas livres: 4
estacao id 38: Instituto dos Cegos - Instituto dos Cegos - Canteiro Central da Avenida Bezerra de Menezes, 801 / Esquina Rua Padre Anchieta / bikes disponiveis: 9, vagas livres: 3
estacao id 41: Érico Mota - Esquina com a Rua Eduardo Barros Leal - Avenida Bezerra de Menezes, 2080 / Esquina Rua Eduardo Barros Leal / bikes disponiveis: 11, vagas livres: 1
estacao id 42: North Shopping - North Shopping - Avenida Bezerra de Menezes, 2500  bikes disponiveis: 4, vagas livres: 8
foram mostradas 4 estacoes

```

Todo o codigo é um enorme draft, foi criado apenas para testar o hook de checar uma bike disponível em loop de tempo, e tem muito espaço para melhorias. Quem achar divertido, brinca um pouco e faz um pull request ;D

### be happy
