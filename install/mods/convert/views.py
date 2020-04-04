from django.shortcuts import render
from rest_framework import viewsets
from django.urls import include, path
import urllib
#from .serializers import CurConvSerializer
#from .models import CurRate
from django.http import HttpResponse, HttpRequest
import json
import traceback
#import urllib.request
import xml.etree.ElementTree as ET
from datetime import date

# Create your views here.
tree = [[]]
out_json = {}
exit_now = "False"
#class curconvViewSet(viewsets.ModelViewSet):
#    queryset = CurRate.objects.all().order_by('Rdate', 'Cur')
#    serializer_class = CurConvSerializer


def Read_Exchange_Rate_Data():
    global document
    global tree
    try:

        url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'
        dbug("RD", [url])
        document = urllib.request.urlopen(url).read()
        tree = ET.fromstring(document)
    except Exception as e:
        dbug("err", ["Exit", "Can't connect to url. " + str(e)])
        print(traceback.format_exc())

def Find_Rate(ref_date, amt, from_cur, to_cur):
    global amount
    global tree

    try:
        count = 0
        to_rate, from_rate = 0, 0
        dbug("FR", [ref_date, from_cur, to_cur, amt])
        if from_cur == to_cur == "EUR":
            amount = float(amt)
            return
        if from_cur == "EUR" or to_cur == "EUR":
            count += 1
        dbug("FR", [ref_date, from_cur, to_cur, amt])
        print(ref_date)
        print("I give up")
       # x = []
        x = tree.find('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube//*[@time="' + str(ref_date) + '"]')
        if x is None:
            dbug("err", ["Exit", "No rate found for date " + str(ref_date) + ". Try a different date"])
            return
        print(ref_date, len(x))
        print("past check")
        for y in range(len(x)):
            if str(x[y].attrib["currency"]) == from_cur:
                from_rate = x[y].attrib["rate"]
                count += 1
            if str(x[y].attrib["currency"]) == to_cur:
                to_rate = x[y].attrib["rate"]
                count += 1
            if count > 1:
                if from_cur == "EUR":
                   amount = (float(amt) * float(to_rate))
                elif to_cur == "EUR":
                   amount = (float(amt) / float(from_rate))
                else:
                   amount = (float(amt) / float(from_rate) * float(to_rate))
                dbug("FR", [ref_date, from_cur, to_cur, amount])
                return str(amount)
    except Exception as e:
        dbug("err", ["Exit", "Can't complete the conversion. " + str(e)])
        #print(traceback.format_exc())

def dbug(section, lst):
    global out_json
    global exit_now
#    return
    if section == "req":
        req = {"requestData": {"referenceDate": lst[0], "srcCurrency": lst[1], "destCurrency": lst[2], "amount": lst[3]}}
        out_json = {**out_json, **req}
    if section == "err":
        exit_now = True
        err = {"errorData": {"errorCode": lst[0], "errorData": lst[1]}}
        out_json = {**out_json, **err}
        return
    if section == "RD":
        rd = {"readData": {"rateURL": lst[0]}}
        out_json = {**out_json, **rd}

    if section == "FR":
        fr = {"findRates": {"referenceDate": lst[0], "srcCurrency": lst[1], "destCurrency": lst[2], "amount": lst[3]}}
        out_json = {**out_json, **fr}

def list(request):
    global amount
    global out_json
    global exit_now

    exit_now = False
    debug = request.GET.get('debug', 0)
    reference_date = request.GET.get('date', date.today().strftime('%Y-%m-%d'))
    src_currency = request.GET.get('from', 'EUR')
    src_currency = src_currency.upper()
    dest_currency = request.GET.get('to', 'EUR')
    dest_currency = dest_currency.upper()
    amount = request.GET.get('amt', 1)
    dbug("req", [reference_date, src_currency, dest_currency, amount])
    Read_Exchange_Rate_Data()
    Find_Rate(reference_date, amount, src_currency, dest_currency)

    amount = round(float(amount),4)
    x = {}
    if exit_now == True:
        y = out_json
    else:
        x = {"Amount": amount, "Currency": dest_currency}
        if debug == "1":
            y = {**out_json, **x}
        else:
            y = x

    print(json.dumps(y, indent=2, sort_keys=False))
    return HttpResponse(json.dumps(y, indent=2, sort_keys=False))

