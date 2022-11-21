#!/usr/bin/env bash
# Reed Posehn, 2022
# API by Yahoo Finance, registration required for API Key
# Dependencies: Curl

echo 'Running Market Summary...'

apiKey=$(cat apiKey.txt)

if [ $# -eq 0 ]
then
	cmd= $(curl -X "GET" "https://yfapi.net/v6/finance/quote/marketSummary?lang=en&region=US" -H "accept: application/json" -H "X-API-KEY: ${apiKey}" > out.json)
else
	sym=$1
	cmd= $(curl -X "GET" "https://yfapi.net/v6/finance/quote?lang=en&region=US&symbols=${sym}" -H "accept: application/json" -H "X-API-KEY: ${apiKey}" > out.json)

fi

python3 Summarize.py out.json

#end
