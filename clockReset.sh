#!/bin/bash

sudo ifconfig eth0 down
sudo service ntp stop
sudo ntpd -gq
sudo service ntp start
sudo ifconfig eth0 up