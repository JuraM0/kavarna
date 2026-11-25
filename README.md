#kavarna

(R8)
Web kavárny vytvořený ve Flasku. Aplikace představuje kavárnu, její nabídky kávy, čaje a
sladkostí, otevírací dobu a kontaktní informace.

(R9)
# demo

## Vytvoření virtuálního prostředí

```shell
python -m venv .venv
```

`-m` python modul - zde se jmenuje `venv`

`.venv` název adresáře s virtuálním prostředím

## Aktivace prostředí

```shell
.venv\Scripts\activate.bat
```

## Instalace frameworku Flask

```shell
pip install Flask
```

## Spuštění aplikace

Výchozí soubor s aplikací se jmenuje `index.py`.

```shell
flask --app index run --debug
```

## Vytvoření requirements.txt

Abychom dokázali zpětně vytvořit virtuální prostředí ve kterém jsme aplikaci vyvíjeli.

```shell
pip freeze
```
