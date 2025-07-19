# TO EXPORT AS STATIC WEBPAGE
`
python .\nightreigncs\manage.py collectstatic
python .\nightreigncs\manage.py distill-local
`

In the created file, some references have to be changed:

- `/static/` becomes `static/`
- `/media/` becomes `media/`