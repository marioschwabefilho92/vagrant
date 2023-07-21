#!/bin/bash
app_name=$1
if [ -z "$app_name" ];
then
  echo "\$app_name is empty, nothing to be done"
else
  favorite_apps=$(gsettings get org.gnome.shell favorite-apps)
  if [ "$favorite_apps" == "@as []" ];
  then
    gsettings set org.gnome.shell favorite-apps "['$app_name']"
  else
    gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed s/.$//), '$app_name']"
  fi
fi
