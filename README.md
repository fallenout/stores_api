

## Installation
#  docker build -t store_rest .
#  docker run -p 5001:5000 store_rest


## Usage
Sono presenti i  due endpoint da testare:

 /stores  (da chiamre con metodo POST ed il body contenente il json sample) 
  i dati vengono memorizzati sulle due tabelle presenti sul db  (stores ed info ) collegate da una relazione 1 a 1


 /stores  (da chiamre con metodo GET) Rrestituisce la lista degli stores contenuti nella tabella stores e le relative informazioni presenti per ogni stores sulla tabella infos






