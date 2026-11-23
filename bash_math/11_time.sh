#!/bin/bash
# Перевод секунд в часы, минуты, секунды
read -p "Введите количество секунд: " total

hours=$((total / 3600))
remainder=$((total % 3600))
minutes=$((remainder / 60))
seconds=$((remainder % 60))

echo "---"
echo "$total секунд = $hours ч $minutes мин $seconds с"