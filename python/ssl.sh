#!/usr/bin/env bash

# Use:  /c/Program\ Files/Git/usr/bin/openssl req -new ... on Windows to avoid 'C:/Program Files/Git/' being concatenated and affixed
## openssl req -new -sha256 -subj ... otherwise
echo "Generating new SSL..." && cd auth && 
openssl genrsa -out key.pem 2048 && 
/c/Program\ Files/Git/usr/bin/openssl req -new -sha256 -subj "/C=US/ST=IL/O=Blah/localityName=Champaign/commonName=Nametag/organizationalUnitName=Nametag/emailAddress=adam.intae.gerard@protonmail.com" -key key.pem -out csr.csr && 
openssl req -x509 -sha256 -days 30 -key key.pem -in csr.csr -out certificate.pem &
