#!/usr/bin/python
from EchoClient import WhatsappEchoClient
import argparse, base64, sys

parser = argparse.ArgumentParser(description = 'Envia missatges per WhatsApp')
parser.add_argument('-t', '--telefon', help = 'telefon')
parser.add_argument('-m', '--missatge', help = 'missatge')
args = parser.parse_args()

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

phone = args.telefon
message = args.missatge

login = #countrycode+phone
password =

wa = WhatsappEchoClient(phone, message)
wa.login(login, base64.b64decode(bytes(password.encode('utf-8'))))
