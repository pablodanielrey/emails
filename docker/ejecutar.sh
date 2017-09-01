#!/bin/bash
sudo docker run -ti -d --name emails -v $(pwd)/src:/src -p 5025:5000 -p 5026:5001 -p 5027:5002 -p 5028:5003 --env-file $HOME/gitlab/fce/produccion/emails emails
sudo docker exec -t emails bash instalar.sh

