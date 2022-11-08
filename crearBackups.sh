#!/bin/bash
 
# The source path to backup. Can be local or remote.
FUENTE=/home/darkaleja/Seguridad/
# Where to store the incremental backups
DESTBASE=/var/tmp/Backups
 
# Where to store today's backup
DESTINO="$DESTBASE/$(date +%d-%m-%Y)"
# Where to find yesterday's backup
AYER="$DESTBASE/$(date -d yesterday +%d-%m-%Y)/"
 
# Use yesterday's backup as the incremental base if it exists
if [ -d "$AYER" ]
then
	OPCIONES="--link-dest $AYER"
fi
 
# Run the rsync
rsync -av $OPCIONES "$FUENTE" "$DESTINO"
