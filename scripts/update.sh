#!/bin/bash

mkdir -p rules

wget -O rules/geosite.dat https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geosite.dat
wget -O rules/geoip.dat https://raw.githubusercontent.com/Loyalsoldier/geoip/release/geoip.dat

python3 scripts/merge.py