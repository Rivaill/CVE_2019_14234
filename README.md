# CVE_2019_14234

`python 2.7.x`
```bash
pip install requirements.txt
```

```bash
vim app/settings.py # update DATABASES
```

```bash
python manage.py migrate
```

```bash
python manage.py makemigrations TestModel
```

```bash
python manage.py migrate TestModel
```

```bash
python PoC.py
```