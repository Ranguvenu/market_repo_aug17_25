#Operational Functions
import sys
sys.path.append('/var/www/html/market/')  
from smartapi import SmartConnect
from config import *
import pyotp, time

#The Connection
def Strategy(CLtp, PriceA=False, PriceB=False, PriceC=False, PriceD=False, PriceE=False, PriceF=False, PriceG=False):
    static i=0
    
    if PriceA < CLtp:



