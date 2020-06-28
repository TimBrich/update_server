CREATE OR REPLACE PROCEDURE create_user(user_name text, user_password text) AS
$$
BEGIN
   IF NOT EXISTS (
      SELECT                       -- SELECT list can stay empty for this
      FROM   pg_catalog.pg_roles
      WHERE  rolname = user_name) THEN

      EXECUTE format('CREATE ROLE %I', user_name);

   END IF;

   EXECUTE format('ALTER USER %I WITH PASSWORD ''%I''', user_name, user_password);
   EXECUTE format('ALTER ROLE %I WITH LOGIN', user_name);
END;
$$
LANGUAGE plpgsql;
