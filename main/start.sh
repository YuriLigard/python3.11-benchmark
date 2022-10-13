#!/bin/bash

export PYTHONPATH="${PYTHONPATH}:$PWD/main"

for algoritmo in Mcarlo
do

    tempoBase="$(docker run -it --rm -v $PWD/main:/main python:$1 /main/medidor.py $algoritmo $2)"

    echo -e "\n=========================================="
    echo "-> Algoritmo: $algoritmo"
    echo "-> Repetições: $2"
    echo "-> Tempo de execução do Python$1: $tempoBase"
    echo -e "==========================================\n"


    for img in 3.7 3.8 3.9 3.10
    do 
        echo "========================"
        echo "-> Versão: Python$img"
        echo "========================"

        tempoExecucao="$(docker run -it --rm -v $PWD/main:/main python:$img /main/medidor.py $algoritmo $2)"
        echo "Execução em: $tempoExecucao"
        res="$(echo "scale=2;(($tempoExecucao - $tempoBase)/$tempoExecucao) * 100" | tr -d $"\r" | bc)"
        echo "Python$1 é $res% mais rápido" 
        
        listaTempoExecucoa+=($tempoExecucao)

        echo -e "------------------------\n" 

    done
    
done
