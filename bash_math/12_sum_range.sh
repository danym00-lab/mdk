#!/bin/bash
# Сумма чисел от 1 до N
read -p "Введите N: " n

sum=0
i=1

while [ "$i" -le "$n" ]; do
    sum=$((sum + i))
    i=$((i + 1))
done

echo "Сумма чисел от 1 до $n = $sum"