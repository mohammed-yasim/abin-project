#!/bin/bash
echo "-------------------------------------"
echo "| DIYA INFO CARE - TERMUX INSTALLER |"
echo "-------------------------------------"
echo " "
echo " "
echo "installing packages.."
echo ""
pkg install python;pip install pip --upgrade;pip install django;pip install plyer;pip install numpy;pip install pandas;pip install django_settings_export;pip install requests;pip install bs4;pip install tabulate
echo 'cd /storage/emulated/0/project;python config.py;python manage.py runserver --insecure;' >> ~/.bashrc;exit;