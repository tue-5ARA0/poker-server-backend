# /bin/sh

python manage.py makemigrations --settings=coonfigurations.dev.settings
python manage.py migrate --run-syncdb --settings=coonfigurations.dev.settings