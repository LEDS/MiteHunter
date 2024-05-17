#!/bin/bash

# Espera 3 minutos
sleep 3m

# Insere no Database
cat backup.sql | docker exec -i mysql /usr/bin/mysql -u root --password=12345 MiteHunter
