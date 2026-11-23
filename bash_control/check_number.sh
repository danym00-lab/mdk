#!/bin/bash
# Задание 3: Проверка числа
# Принимает число как аргумент и определяет его знак

if [ -z "$1" ]; then
    echo "Ошибка: передайте число аргументом. Пример: ./check_number.sh -5"
    exit 1
fi

number=$1

if ! [[ "$number" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
    echo "Ошибка: '$number' не является числом."
    exit 1
fi

if (( $(echo "$number > 0" | bc -l) )); then
    echo "Число $number является положительным"
elif (( $(echo "$number < 0" | bc -l) )); then
    echo "Число $number является отрицательным"
else
    echo "Число $number является нулём"
fi