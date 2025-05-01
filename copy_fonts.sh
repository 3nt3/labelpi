#!/bin/sh

all_font_files=""
while read font; do
    # find all font files
    # echo $font
    font_files=`fc-list | rg "$font" | sed 's/:.*$//' `

    echo "$font_files"

    # add to all_font_files
    all_font_files="$all_font_files\n$font_files"
done < fonts.txt

mkdir /tmp/labelpi-fonts

printf "%b\n" "$all_font_files" | sed '/^$/d' | while IFS= read -r file; do
    cp "$file" /tmp/labelpi-fonts/
done

tar cJf fonts.tar.xz /tmp/labelpi-fonts
