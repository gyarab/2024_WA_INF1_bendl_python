# 2024_WA_INF1_bendl_python
Pro spuštění ujistit se že máme nainstalovaný vše z requirements.txt. Dále v konzoli aktivujeme virtuální prostředí, načtení migrací a fixtures a zapneme lokální server.

## aktivace prostředí 
(v mém případě venv)

    ./venv/Scripts/activate
## provedení migrací
    python manage.py migrate
## načtení fixtures
    python manage.py loaddata selected_models.json¨
případně pro smazání:

    python manage.py flush 
## spuštění lokálního serveru
    python manage.py runserver
