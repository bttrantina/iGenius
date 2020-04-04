![GitHub Logo](install/igbtt.png)
# Repo prepared for iGenius

Challenge was to build application to convert currency based upon rates avaialable from:
   https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml 

## Parameters provided include:

Design an endpoint to receive:
   * amount - the amount to convert (e.g. 12.35) 
   * src_currency - ISO currency code for the source currency to convert (e.g. EUR, USD, GBP) 
   * dest_currency - ISO currency code for the destination currency to convert (e.g. EUR, USD, GBP)
   * reference_date - reference date for the exchange rate, in YYYY-MM-DD format

## Endpoint must:

* Convert the provided amount from src_currency to dest_currency using rates on the given refernce date

## Response should return the destination currency and the converted currency amount:

{     “amount”: 20.23,     “currency”: ”EUR” }

## Components supporting the application:
*   Python3
*   Django
   
## Instructioins to install and set up the application

Install procedures are wrtten for Windows 10 desktop.

Open a command prompt
click on search bar and enter:
cmd \<enter\>

Make sure python 3.x is installed:
python --version \<enter>

Make folder/directory in write accessible drive, using "btt_ig" as an example:

mkdir btt_ig  \<enter>

Change directory into that new directory:

cd btt_ig

Pull down install folder from GitHub:

Click on GitHub link to open application repository. 
Click on "Clone or download" button on the right side of panel.
Select "Download Zip" option to download package to your machine.
Copy the "install" folder from the zip file to the directory you created above.

Change directory into the install folder:
cd install

Execute batch files in order:

	1_startenv.batch.bat 
	2_install_django.bat
	3_copy_modules.bat 
	4_startserver.bat
	5_curl_tests.bat
	
Start virtual environment:

1_startenv.batch.bat \<enter>

Install Django components:

2_install_django.bat \<enter>

Copy the Convert application to Django location:

3_copy_modules.bat \<enter>

Start the Django server and second command prompt:
4_startserver.bat \<enter>

## Test the application using curl:
TEST the API using Curl commands -
Go to the second command prompt can execute curl test:

5_curl_tests.bat \<enter>

## Test the application using web browser:
TEST the API from web browser - 
Open web browser and copy/paste the address below:

http://127.0.0.1:8000/convert/?date=2020-03-31&from=usd&to=jpy&amt=4325.65

Try other dates/currencies/amounts as you like.
if no "date=" parameter is provided, current date is used.

## Debug feature: 
There is also a debug parameter available, add "&debug=1" to your request to see the results.  Debug is automatically turned on if an error occurs, such as an invalid date.

Cheers!
