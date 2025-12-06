#!/bin/bash

set -x

cp $(ls [0-9]*.py |tail -n1) a

curl \
	--silent \
	--user-agent 'curl by github.com/arichnad' \
	https://adventofcode.com/2025/stats |
	grep 'a href.*stats-both' |
	head -n 1 |
	tee --append .place

