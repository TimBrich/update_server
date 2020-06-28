python3 manage.py makemigrations
python3 manage.py migrate

echo "create superuser..."
cat create_super_user.py | python3 manage.py shell
