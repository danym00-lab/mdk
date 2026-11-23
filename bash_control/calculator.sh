#!/bin/bash
# Задание 2: Калькулятор
# Запрашивает два числа и операцию, выводит результат

read -p "Введите первое число: " num1
read -p "Введите второе число: " num2
read -p "Введите операцию (+, -, *, /): " op

# Проверка, что введены числа
if ! [[ "$num1" =~ ^-?[0-9]+([.][0-9]+)?$ ]] || ! [[ "$num2" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
    echo "Ошибка: нужно ввести числа."
    exit 1
fi

case "$op" in
    +) result=$(echo "$num1 + $num2" | bc) ;;
    -) result=$(echo "$num1 - $num2" | bc) ;;
    \*) result=$(echo "$num1 * $num2" | bc) ;;
    /)
        if [ "$num2" == "0" ]; then
            echo "Ошибка: деление на ноль."
            exit 1
        fi
        result=$(echo "scale=2; $num1 / $num2" | bc)
        ;;
    *)
        echo "Ошибка: неизвестная операция."
        exit 1
        ;;
esac

echo "Результат: $num1 $op $num2 = $result"