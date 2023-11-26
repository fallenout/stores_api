

## Installation
- docker build -t store_rest .
- docker run -p 5001:5000 store_rest


## Usage
Sono presenti i due endpoint da testare:

  - http://127.0.0.1:5001/stores  (da chiamre con metodo POST ed il body contenente i dati presenti in  sample.json) 
 i dati vengono memorizzati sulle due tabelle presenti sul db  (stores ed info ) collegate da una relazione 1 a 1



  - sshttp://127.0.0.1:5001/stores (da chiamre con metodo GET)
 
 Restituisce la lista degli stores contenuti nella tabella stores e le relative informazioni presenti per ogni stores sulla tabella infos






