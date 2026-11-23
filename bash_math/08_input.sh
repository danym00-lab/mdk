#!/bin/bash
# Спрашиваем числа у пользователя
read -p "Введите первое число: " a
read -p "Введите второе число: " b

sum=$((a + b))
diff=$((a - b))
prod=$((a * b))

echo "---"
echo "Сумма: $sum"
echo "Разность: $diff"
echo "Произведение: $prod"

if [ "$b" -ne 0 ]; then
    echo "Деление: $((a / b))"
    echo "Остаток: $((a % b))"
else
    echo "Деление на ноль невозможно"
fi