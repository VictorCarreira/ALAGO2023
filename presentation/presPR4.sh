#!/bin/bash

# makes this shell executable and after that execute it:
# chmod +x filename.sh
# ./filename.sh

aspell check -l pt presPR4.tex

pdflatex presPR4.tex

bibtex references.bib

pdflatex presPR4.tex

pdflatex presPR4.tex

okular presPR4.pdf

# Corretor ortográfico no vim:
#:set spell spelllang=en
#:set spell spelllang=pt

#Em modo visual os comandos:
# ]s vai para a próxima palavra;
# [s vai para a palavra anterior;
# z= mostra a lista de sugestões para a palavra;
# zg adiciona a palavra sob o cursor no dicionário, assim ela não será mais marcada como errada;
# zug desfaz a última palavra adicionada;
# zw remove a palavra sob o cursor do dicionário, assim ela será marcada como errada;
# zuw desfaz a última palavra removida.

# para sair:
# :set nospell

# aspell check -l en methods.tex 


rm presPR4.log presPR4.aux  presPR4.nav presPR4.out presPR4.snm presPR4.toc
