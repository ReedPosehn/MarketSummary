import sys
import json

if len(sys.argv) > 1:
    file = open(sys.argv[1])
    #json_str = file.read()
    #json_str = sys.argv[1]
    data = json.load(file)
    if "marketSummaryResponse" in data:
        marketResp = data["marketSummaryResponse"]['result']
        for item in marketResp:
            if 'shortName' in item:
                print(item['fullExchangeName'] + ' - ' + item['shortName'])
            else:
                print(item['fullExchangeName'])
            print("Regular Market Change Percent - " + item['regularMarketChangePercent']['fmt'])
            print("Regular Market Previous Close - " + item['regularMarketPreviousClose']['fmt'])
            print("Regular Market Change - " + item['regularMarketChange']['fmt'])
            print('Regular Market Price - ' + item['regularMarketPrice']['fmt'])
    else:
        quoteResp = data["quoteResponse"]['result'][0]
        print(quoteResp['symbol'] + ' - ' + quoteResp['shortName'])
        print("Regular Market Change Percent - " + str(quoteResp['regularMarketChangePercent']))
        print("Regular Market previous Close - " + str(quoteResp['regularMarketPreviousClose']))
        print("Regular Market Change - " + str(quoteResp['regularMarketChange']))
        print("Regular Market Price - " + str(quoteResp['regularMarketPrice']))
        
    file.close()
else:
    print('No arguments provided!')
