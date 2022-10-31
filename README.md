# Data API Explorer

## Overview
This is a simple project that creates a table in Redshift with some fake test data and then interacts with the Redshift instance via the Redshift Data API in Python.

These scripts were used in a blog post that I wrote on my personal website: https://smpotts.github.io/2022-10-27-data-api-demo/

## Structure
[data_setup.sql](redshift_ddl/data_setup.sql): contains the SQL commands to create the database, schema and table in Redshift and then insert test data into it.
[main.py](main.py): a simple python method that runs the API commands to interact with the Redshift Data API and prints out the response objects.