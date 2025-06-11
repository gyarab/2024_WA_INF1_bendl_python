# DaSiHa - knihovna videoherních miniprojektů
    Tato knihovnička má zpřehednit a zdostupnit naše ročníkové projeky, psané v JavaScriptu s arkádovým kabátkem retro her.
---
## Struktura datového modelu
### Genre (Herní žánr)
* Reprezentuje žánr, do kterého může hra spadat
* Obsahuje atribut `name` (název žánru)
* Vztah **M:N** s modelem **Game** (jedna hra může patřit do více žánrů).

### Author (Autor)
* Reprezentuje autora nebo tým autorů, kteří vytvořili hru.
* Obsahuje atribut `name` (jméno autora).
* Vztah **M:N** s modelem **Game** (podporuje spoluautorstvý).

### Game (Herní titul)
* Reprezentuje jednotlivou hru uloženou v systému.
* Obsahuje atributy:
  - `name` (název hry)
  - `descript` (popis hry)
  - `code_path` (cesta ke spuštění hry)
  - `needs_login` (zda je potřeba přihlášení ke spuštění)
  - `logo`, `preview`, `thumbnail` (obrázky hry)
  - `favorited_by` (uživatelé, kteří si hru označili jako oblíbenou)
* Vztah **M:N** s **Genre** a **Author**.
* Vztah **1:N** s modelem **Comment**.

### Comment (Komentář)
* Reprezentuje komentář uživatele ke konkrétní hře.
* Obsahuje atributy:
  - `text` (obsah komentáře)
  - `created_at` (datum a čas vložení)
  - `ip_address`, `user_agent` (metadata o zařízení)
* Vztah **N:1** k modelu **Game** (každý komentář náleží jedné hře).
---
### Spuštění
### 1) Aktivace virtuálního prostředí
    ./venv/Scripts/activate
### 2) Instalace requirements.txt
    pip install -r requirements.txt
### 3) Migrace databáze
    python manage.py migrate
### 4) Načtení testovacích dat
    python manage.py loaddata selected_models.json
### 5) Spuštění (lokálního) serveru
    python manage.py runserver
