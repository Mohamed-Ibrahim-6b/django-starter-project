#!.venv/bin/python
import secrets

secret_key = secrets.token_urlsafe(nbytes=38)
print(secret_key)

# or simply run the command
# docker-compose exec web python -c "import secrets; print(secrets.token_urlsafe(38))"
# or
# python -c "import secrets; print(secrets.token_urlsafe(38))"
# or
# python3 -c "import secrets; print(secrets.token_urlsafe(38))"
