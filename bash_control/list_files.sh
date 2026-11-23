#!/bin/bash
# Задание 4: Список .txt файлов
# Принимает путь к директории и выводит .txt файлы с размерами

if [ -z "$1" ]; then
    echo "Ошибка: укажите путь к директории. Пример: ./list_files.sh /home/user/documents"
    exit 1
fi

directory=$1

if [ ! -d "$directory" ]; then
    echo "Ошибка: директория '$directory' не существует."
    exit 1
fi

echo "Найдены .txt файлы в $directory:"
found=0
for file in "$directory"/*.txt; do
    if [ -f "$file" ]; then
        size=$(du -h "$file" | cut -f1)
        echo "- $(basename "$file") ($size)"
        found=1
    fi
done

if [ $found -eq 0 ]; then
    echo "  (файлов .txt не найдено)"
fi