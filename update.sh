#!/bin/bash
sudo systemctl stop siguiente-letra &&
git pull origin master &&
source ./venv/bin/activate &&
pip -r requeriments.txt &&
sudo systemctl start siguiente-letra
