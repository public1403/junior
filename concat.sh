#!/bin/bash

PRE="/var/www/html/"

cat ./base.html     \
./EmbededSystem/es.html \
./tail.html         \
> ./index.html
#./linux/linux.html  \
