# coding:utf-8

import time
import hashlib
import hmac
import base64
import requests
from urllib.parse import quote

HOST = "mws.amazonservices.com"
HTTPMethod = 'POST'
AWSAccessKeyId = "AKIAI4IDB6MWJPVSDKQQ"
SellerId = "A23LGBE17JOXAI"
Marketplace = "ATVPDKIKX0DER"
MWSAuthToken = "amzn.mws.fcafccdc-8aca-0e02-69cb-ca594407d1cf"
SignatureMethod = "HmacSHA256"
SignatureVersion = "2"
Version = "2009-01-01"
ReportType = "_GET_MERCHANT_LISTINGS_DATA_"
SecretKey = "JpN3ZmNiVVdk/x9ce/tsdUN29xsQ75zq3NUDCTL8"
PortPoint = '/Reports/2009-01-01'
Headers = {
            "Host":"mws.amazonservices.com",
            "x-amazon-user-agent": "AmazonJavascriptScratchpad/1.0 (Language=Javascript)",
            "Content-Type": "text/xml",
            "User_Agent":"Data_Force"
            }

# Required parameters for the report
def report(aws_accesskey_id, action, mws_authtoken, seller_id, 
	       signature_version, signature_method, timestamp, version):
    report_dict = {
        'AWSAccessKeyId': aws_accesskey_id,
        'Action': action,
        'MWSAuthToken': mws_authtoken,
        'SellerId': seller_id,
        'SignatureVersion': signature_version,
        'SignatureMethod': signature_method,
        'Timestamp': timestamp,
        'Version': version
    }
    return report_dict

# Request the parameters in the report method
#   and join required parameters for the report
def request_report(report_type):
    action = 'RequestReport'
    timestamp = get_timestamp()
    request_dict = report(AWSAccessKeyId, action, MWSAuthToken, SellerId,
                    SignatureVersion, SignatureMethod, timestamp, Version)
    request_dict['ReportType'] = report_type
    return request_dict

# Generates signature for the url
def get_signature(secret_key, message, sign_mod):
    secret_key = bytes(secret_key, "utf-8")
    message = bytes(message, "utf-8")
    hmac_sign = hmac.new(secret_key, message, digestmod=sign_mod)
    signature = base64.b64encode(hmac_sign.digest())
    signature = str(signature, "utf-8")
    return quote(signature).replace('/', '%2F')

# Generates the current timestamp
def get_timestamp():
    time_stamp = time.localtime()
    month = str(time_stamp[1])
    date = str(time_stamp[2])
    if len(month) == 1:
        month = '0'+ month
    if len(date) == 1:
        date = '0'+ date
    if len(str(int(time_stamp[3])-8)) == 2:
        time_stamp = str(time_stamp[0])+'-'+month+'-'+date+'T'+str(int(time_stamp[3])-8)+':'+str(int(time_stamp[4]))+':'+'00'
    else:
        time_stamp = str(time_stamp[0])+'-'+month+'-'+date+'T'+'0'+str(int(time_stamp[3])-8)+':'+str(int(time_stamp[4]))+':'+'00'

    stmp = time_stamp+'Z'
    return quote(stmp)

# Gets the url of the query request
def get_url():
    request_dict = request_report(ReportType)
    request_sort = sorted(request_dict.items())
    canstring = ''
    for key, value in request_sort:
        canstring += '&' + key + '=' + value
    string_to_sign = HTTPMethod + '\n' + HOST + '\n' + PortPoint + '\n'  + canstring[1:]
    signature = get_signature(SecretKey, string_to_sign, hashlib.sha256)

    canstring += '&Signature=' + signature
    url = "https://" + HOST + PortPoint + "?" + canstring
    return url

# Request the url and get response
if __name__ == "__main__":
    request_report_url = get_url()
    xml = requests.post(request_report_url, headers=Headers)
    print(xml.text)


