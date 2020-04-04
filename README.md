# Repo prepared for iGenius

Challenge was to build application to convert currency based upon rates avaialable from:
   https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml 

## Parameters provided include:
​ : design endpoint to include:
​ : amount - the amount to convert (e.g. 12.35) 
​ : src_currency - ISO currency code for the source currency to convert (e.g. EUR, USD, GBP) 
​ : dest_currency - ISO currency code for the destination currency to convert (e.g. EUR, USD, GBP)
​ : reference_date - reference date for the exchange rate, in YYYY-MM-DD format

## Endpoint must:
​ : Convert the provided amount from src_currency to dest_currency using rates on the given refernce date
​ : NOTE: this endpoint displays an error if rates are not found for a given reference date

The response should be a JSON object like this: 
 
{     “amount”: 20.23,     “currency”: ”EUR” }
Join the slack! <https://join.slack.com/t/findthemasks/shared_invite/zt-czdjjznp-p8~9oKuXtV_gn7wEBZGGoA>

- new dev? please look at issues and comment on something to grab it!
    - Check out the [Getting Started](getting_started.md) doc
- new data moderator? Join the slack and come to #data!
- not either? The most useful contribution is identifying more drop off locations and plugging them into the form linked on the public website, so if you don't see an issue here that calls to you, please work on that! Advice on making calls is in [#131](https://github.com/r-pop/findthemasks/issues/131#issuecomment-602746963)

## Current setup

- The website reads from a google sheet, generates a json blob, which is used to generate static HTML.

## Reading our data to build your own frontend

- Our data file updates every five minutes and can be read from findthemasks.com/data.json.
- If you read the json directly, you need to ignore entries without an 'x' in the first field. Otherwise, you may publish info hospitals asked to have taken down. Don't do it!
- If this sounds like too much work, then please use our:

## Embeddable widget of donation sites
