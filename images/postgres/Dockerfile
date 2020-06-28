FROM postgres:12

COPY scripts/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY scripts/new-docker-entrypoint.sh /usr/local/bin/new-docker-entrypoint.sh
ADD sql/create_user.sql /etc/postgres/create_user.sql

ENTRYPOINT ["new-docker-entrypoint.sh"]
CMD ["postgres"]
