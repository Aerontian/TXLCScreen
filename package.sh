#!/bin/bash

source_path="./FactorTest"
if [ -d "./test_docx" ]; then
	echo "directory test_docx exists"
else
	mkdir test_docx
	echo "test_docx directory is created."
fi
raw_file_list=""
for source_sub_path in $(ls $source_path)
do
	dir="Doc"
	file_docx=${source_path}"/"${source_sub_path}"/"${dir}"/""*.docx"
	cmd="cp -v "${file_docx}$" ./test_docx"
	#echo $cmd
	if [ -e $file_docx ]; then
		eval $cmd
	fi
done
if [ -e "./test_sum.rar"]; then
	rm -v test_sum.rar
fi
rar a test_sum.rar ./test_docx/*.docx
rm -r -v test_docx
