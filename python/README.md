# TheRightParKing
Repositório para a solução do TheRightParKing?

Antes de tudo... use python 2.7...

Instale a sdk do google cloud para python:
https://cloud.google.com/python/

RODE ESTES COMANDOS PARA ATUALIZAR AS LIBS DE SUPORTE DO PYTHON:
 - sudo apt-get install libffi-dev
 - sudo apt-get install libssl-dev
 - sudo apt-get install python-dev
 - pip install setuptools

QUER INTALAR AS DEPENDENCIAS???
 - pip install -t ./lib -r requirements.txt --upgrade

QUER RODAR EM DEV (NA SUA MAQUINA, Meu CHAPA)!?!?
 - dev_appserver.py .

TA RODANDO A APLICAÇÂO LOCAL NENE? ENTÃO:
 - http://localhost:8080/

SE FALHAR POR PERMISSÃO???
 - VERIFIQUE A SUA PERMISSÃO PARA ESTE DIRETÓRIO E CORRIJA:
	/home/[SEU_USUARIO_LOGADO_NA_SUA_MAQUINA]/.config/gcloud

QUER FAZER DEPLOY NO GAE???
 - gcloud app deploy app.yml -v v1
 
SE FALAR QUE VC NÂO TEM PERMISSÃO, APARE SEU OAUTH CACHE:
 - rm ~/.appcfg_oauth2_tokens


