#!/usr/bin/bash

echo "[WARNING] Please run this script as sudo, this script changes the jar file inside /usr/lib/tlauncher"

PREVIOUS_PATH=$(pwd)

echo "[INFO] Creating temporary dir /tmp/tlauncher-update"
mkdir /tmp/tlauncher-update
cd /tmp/tlauncher-update

echo "[INFO] Getting latest version from repo.tlauncher.org..."
wget https://repo.tlauncher.org/update/lch/starter-core-1.11-pre-v8.jar
mv starter-core-*.jar tlauncher.jar

echo ""

echo "[INFO] Removing previous version jar file..."
rm /usr/lib/tlauncher/tlauncher.jar

echo "[INFO] Installing latest version to /usr/lib/tlauncher..."
mv tlauncher.jar /usr/lib/tlauncher

echo "[INFO] Cleaning temporary files..."
rm -rf /tmp/tlauncher-update

echo ""

cd $PREVIOUS_PATH

echo "Done! If you encounter any issues when running this script, describe your problem at https://github.com/retrozinndev/tlauncher-copr/issues/new"

