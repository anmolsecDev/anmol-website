#!/bin/bash
set -xe
sudo apt install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
tar -xvzf geckodriver-v0.31.0-linux64.tar.gz
rm geckodriver-v0.31.0-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/