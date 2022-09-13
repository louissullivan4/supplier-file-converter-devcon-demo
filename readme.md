# How to run

## Locally

1. Clone the repository and `cd` into it.
2. Open a terminal and run `pip install -r requirments.txt`
3. Once complete, run `flask run`
4. Open a seperate terminal and run `curl --output final.xlsx -X POST http://127.0.0.1:5000/upload -H "Content-Type: multipart/form-data" -F "file=@supplier_product_list.xlsx"`. Ensure that the server you are connecting to is the one your flask server is running on.
5. Open your new `final.xlsx` file

## Server

1. Clone the repository or make sure you have a copy of the `supplier_product_list.xlsx` in your active directory.
2. Open a terminal and run the command `curl --output final.xlsx -X POST http://sullivls.pythonanywhere.com/upload -H "Content-Type: multipart/form-data" -F "file=@supplier_product_list.xlsx"`
3. Open your new `final.xlsx` file
