### Project: Capital Finder

Author: Lauren 

Version: 1.0

Links and Resources

Special thanks to REST Countries: https://restcountries.com/#rest-countries

#### Overview

Use the requests library to interact with REST Countries API

Create a serverless function to handle two types of queries: 

The capital of Chile is Santiago.

Santiago is the capital of Chile.

This implementation also handles: 

Countries with multiple capitals.

Queries with a country and a capital at the same time. 



#### To initialize

Visit my Vercel site: https://capital-finder-git-main-elleem.vercel.app/

Add on the pathway api/define? 

The keywords to structure your search are country= and capital= 

link country and capital with & to run both search terms. 

#### Tests

Test to look up a country: 

https://capital-finder-elleem.vercel.app/api/define?country=France

Test to look up a capital: 

https://capital-finder-elleem.vercel.app/api/define?capital=Amsterdam

Test to look up multiple capitals: 

https://capital-finder-elleem.vercel.app/api/define?country=South%20Africa

Test to look up capital and country and validate a correct entry: 

https://capital-finder-elleem.vercel.app/api/define?capital=Ottawa&country=Canada

Test to look up capital and country and validate an incorrect entry: 

https://capital-finder-elleem.vercel.app/api/define?capital=Vancouver&country=Canada

