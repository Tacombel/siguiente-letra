#!/bin/bash
sudo systemctl stop siguiente-letra &&
git pull origin master &&
source /home/ubuntu/www/siguiente-letra/venv/bin/activate &&
pip -r requeriments.txt &&
sudo systemctl start siguiente-letra
