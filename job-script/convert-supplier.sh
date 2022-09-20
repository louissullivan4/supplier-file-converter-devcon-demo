#!/bin/bash

rm -r final.xlsx supplier_product_list.xlsx > /dev/null 2>&1
curl --output supplier_product_list.xlsx -X GET https://raw.githubusercontent.com/louissullivan4/supplier-file-converter-devcon-demo/server/master/supplier_product_list.xlsx
curl --output final.xlsx -X POST http://sullivls.pythonanywhere.com/upload -H "Content-Type: multipart/form-data" -F "file=@supplier_product_list.xlsx"
