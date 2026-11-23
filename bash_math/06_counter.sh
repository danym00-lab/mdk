#!/bin/bash
# Счётчик с разными способами увеличения
count=0

count=$((count + 1))
echo "После первого увеличения: $count"

(( count++ ))
echo "После второго увеличения: $count"

(( count += 5 ))
echo "После += 5: $count"

(( count *= 2 ))
echo "После *= 2: $count"