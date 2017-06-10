from lightbulb.api.api_native import LightBulb
import base64

lightbulbapp = LightBulb()
path = "/test/env/bin/lightbulb"  #Path to binary

configuration_A = {'TESTS_FILE_TYPE': 'None', 'ALPHABET': '32-57,58-64,65-126', 'SEED_FILE_TYPE': 'FLEX', 'TESTS_FILE': 'None','DFA1_MINUS_DFA2': 'True', 'SAVE': 'False', 'HANDLER': 'None', 'SEED_FILE': '{library}/regex/BROWSER/html_p_attribute.y'}
configuration_B = {'TESTS_FILE_TYPE': 'None', 'ALPHABET': '32-57,58-64,65-126', 'SEED_FILE_TYPE': 'FLEX', 'TESTS_FILE': 'None','DFA1_MINUS_DFA2': 'True', 'SAVE': 'False', 'HANDLER': 'None', 'SEED_FILE': '{library}/regex/BROWSER/html_p_attribute.y'}
handlerconfig_A = {'WSPORT': '9900','WBPORT': '9980', 'BROWSERPARSE': 'True', 'DELAY': '50', 'HOST': 'localhost'}
handlerconfig_B = {'MESSAGE':   base64.b64encode(bytes("""GET /~fishingspot/securitycheck/index.php?koko=--LIGHTBULB--REPLACE--HERE-- HTTP/1.1
Host: 127.0.0.1
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
DNT: 1
Accept-Language: en-US,en;q=0.8
Connection: close

""")),
    'HOST':'127.0.0.1', 'PORT':'80', 'HTTPS':'False', 'BLOCK':'Impact', 'BYPASS':'None'}


stats = lightbulbapp.start_sfadiff_algorithm(
	path,
    configuration_A,
    configuration_B,
    handlerconfig_A,
    handlerconfig_B,
    "BrowserHandler",
    "RawHTTPHandler")

print stats

