#!/bin/bash
# Переменные и подстановка
price=150
quantity=3
total=$((price * quantity))

echo "Цена: $price руб."
echo "Количество: $quantity шт."
echo "Итого: $total руб."
echo "---"

quantity=5
total=$((price * quantity))
echo "После изменения количества:"
echo "Количество: $quantity шт."
echo "Итого: $total руб."