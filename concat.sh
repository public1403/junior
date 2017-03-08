#!/bin/bash

PRE="/var/www/html/"

cat ./base.html     \
./linux/linux.html  \
./EmbededSystem/es.html \
./tail.html         \
> ./index.html
