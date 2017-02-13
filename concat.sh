#!/bin/bash

PRE="/var/www/html/"

cat ./base.html     \
./DIP/dip.html      \
./linux/linux.html  \
./tail.html         \
> ./index.html
