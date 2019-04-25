# Teste de Seleção: Serviço Flask para Desenho Molecular

Existem inúmeras maneiras se representar moléculas. Uma destas formas consiste em empregar uma série de regras para escrever, literalmente, a fórmula molecular por extenso, preservando, inclusive as ligações e ordem entre os átomos. Este sistema é chamado de Simplified molecular-input line-entry system ​(SMILES).

## Como usar

Para utilizar este sistema, é necessário clonar este repositório:

```
$ git clone git://github.com/Niaev/teste-de-selecao_altox
```

É necessário, também, instalar os seguintes *frameworks*:

* flask
* rdkit

Depois, basta digitar, no seu terminal os seguintes comandos, no diretório do clone deste repositório:

```
$ FLASK_APP=index.py
$ flask run
```

E então, digite na barra de pesquisa do seu navegador ```127.0.0.1:5000/drawMolecule/<molecula>```, sendo ```<molecula>``` uma fórmula molecular. Ao apertar o botão ```Enter```, uma imagem como resultado deverá aparecer.