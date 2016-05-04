# ITSubscriber
Proyecto Integrador 2 API

##TODO
- [x] Token y permisos especificos
- [x] "Login"
- [x] Modelos
- [x] ModelViewSets
- [x] Montar en alguna parte
- [ ] TestsCases
- [ ] Motivacion
- [ ] ...


# Instalacion
1. Instalar virtualenvwrappper (opcional)
2. mkvirtualenv --python=/usr/bin/python3 nameOfEnvironment
3. workon nameOfEnvironment
4. pip install -r requirements.txt

# Correr localmente

- Descomentar
```python
DATABASES = {
    'default': {
        # 'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

- Comentar
```python
DATABASES['default'] =  dj_database_url.config()
```

- Correr migraciones y levantar servidor
```python
$ python manage.py migrate
$ python manage.py runserver	
```

# Crear superadmin
```python
python manage.py createsuperuser
```