#!/bin/bash

echo "---Calculadora Simples---"
echo "Olá, digite o primeiro número: "
read num1
echo "Digite o segundo número: "
read num2


echo -e "\n--- MENU DE OPERAÇÕES ---"
echo -e " [+] Soma\n [-] Subtração\n [*] Multiplicação\n [/] Divisão"
echo "---------------------------"
read operador


case $operador in
	+) resultado=$(echo "$num1 + $num2" | bc -l) ;;
	-) resultado=$(echo "$num1 - $num2" | bc -l) ;;
	"/")
		if [ $num2 -eq 0 ]; then
			resultado="Erro: Divisão por zero!"
		else
			resultado=$(echo "scale=2; $num1 / $num2" | bc -l)
		fi
		;;
	"*") resultado=$(echo "$num1 * $num2" | bc -l) ;;
	*) resultado="Operação Inválida" ;;
esac

echo "O resultado é : $resultado"
