#!/bin/bash


read -p 'Please enter an image name: ' varimage

read -p 'Please enter a tag name (latest, v1): ' vartag
echo
echo Command will be Docker build -t $varimage:$vartag .
exec Docker build -t $varimage:$vartag .
