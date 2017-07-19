# /bin/bash -e

sudo apt-get -y install unixodbc
sudo apt-get -f install
sudo apt-get -y install unixodbc-dev
wget https://packages.microsoft.com/ubuntu/16.04/prod/pool/main/m/msodbcsql/msodbcsql_13.1.9.0-1_amd64.deb

dpkg -i msodbcsql_13.1.9.0-1_amd64.deb

