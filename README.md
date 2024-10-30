
# Lumenpudotuspalvelun varausjärjestelmä

Tämä projekti on yksinkertainen varausjärjestelmä, jossa käyttäjät voivat tilata lumenpudotuspalvelun omakotitalon katolta. 
Palvelua on saatavilla arkisin klo 8–16 välillä.


## Käyttöohjeet

1. Asenna riippuvuudet:
    ```bash
    pip install -r requirements.txt
    ```

2. Aja tietokannan migraatiot:
    ```bash
    python manage.py migrate
    ```

3. Käynnistä palvelin:
    ```bash
    python manage.py runserver
    ```

4. Käyttöliittymä löytyy osoitteesta:
    `http://localhost:8000`

## Tietokanta

Tietokanta sisältää seuraavat taulut:

- **Users**: käyttäjät, jotka tilaavat lumenpudotuksen
- **Orders**: tilaukset, joista jokainen sisältää tiedot ajankohdasta ja käyttäjästä

## SQL esimerkkejä

### Esimerkki SELECT kyselyistä

1. Kaikki tilaukset:
    ```sql
    SELECT * FROM orders;
    ```

2. Tilaukset tietyltä päivältä:
    ```sql
    SELECT * FROM orders WHERE date = '2024-01-10';
    ```

3. Kaikki käyttäjät, jotka ovat tehneet tilauksia:
    ```sql
    SELECT users.name, COUNT(orders.id) FROM users
    JOIN orders ON users.id = orders.user_id
    GROUP BY users.name;
    ```

