#!/bin/bash

/usr/local/bin/docker-entrypoint.sh "$@"


create_user()
{
    psql --username "root" -c "CALL create_user('$1','$2');"
    echo "SELECT 'CREATE DATABASE $3' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$3')\gexec" | psql --username "root"
    psql --username "root" -c "GRANT ALL PRIVILEGES ON DATABASE $3 TO $1"
}

# allow the container to be started with `--user`
if [ "$1" = 'postgres' ] && [ "$(id -u)" = '0' ]; then
	exec gosu postgres "$BASH_SOURCE" "$@"
fi

PGUSER="${PGUSER:-$POSTGRES_USER}" pg_ctl -D "$PGDATA" -o "-c listen_addresses=''" -w start

psql --username "root" -f /etc/postgres/create_user.sql
create_user "$ESP_UPDATE_SERVER_USER" "$ESP_UPDATE_SERVER_PASSWORD" "$ESP_UPDATE_SERVER_DATABASE"

PGUSER="${PGUSER:-$POSTGRES_USER}" pg_ctl -D "$PGDATA" -m fast -w stop
exec "$@"
