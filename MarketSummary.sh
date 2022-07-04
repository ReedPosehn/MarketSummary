#!/usr/bin/env bash
# Reed Posehn, 2022
# API by Yahoo Finance, registration required for API Key
# Dependencies: Curl

echo 'Running Market Summary...'

apiKey=$(cat apiKey.txt)

cmd= curl -X "GET" "https://yfapi.net/v6/finance/quote/marketSummary?lang=en&region=US" -H "accept: application/json" -H "X-API-KEY: ${apiKey}"

#end
