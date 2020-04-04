REM valid date tests:
curl "http://127.0.0.1:8000/convert/?date=2020-03-30&from=USD&to=EUR&amt=11.53"

curl "http://127.0.0.1:8000/convert/?date=2020-03-30&from=USD&to=EUR&amt=11.53&debug=1"

curl "http://127.0.0.1:8000/convert/?date=2020-03-30&from=eur&to=EUR&amt=11.53&debug=1"

curl "http://127.0.0.1:8000/convert/?date=2020-03-30&from=USD&to=jpy&amt=1231.53"

curl "http://127.0.0.1:8000/convert/?date=2020-03-30&from=USD&to=jpy&amt=1231.53&debug=1"

REM invalid date tests:

curl "http://127.0.0.1:8000/convert/?date=2020-03-29&from=USD&to=EUR&amt=11.53"

curl "http://127.0.0.1:8000/convert/?date=2020-03-29&from=USD&to=EUR&amt=11.53&debug=1"

curl "http://127.0.0.1:8000/convert/?date=2020-03-29&from=eur&to=EUR&amt=11.53&debug=1"

curl "http://127.0.0.1:8000/convert/?date=2020-03-29&from=USD&to=jpy&amt=1231.53"

curl "http://127.0.0.1:8000/convert/?date=2020-03-29&from=USD&to=jpy&amt=1231.53&debug=1"

pause


