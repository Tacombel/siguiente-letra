#!/bin/bash
sudo systemctl stop siguiente-letra &&
git pull origin master &&
/.venv/bin/pip -r requeriments.txt &&
sudo systemctl start siguiente-letra
