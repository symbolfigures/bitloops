The [python version](python) is used for the front end (bitcalctess.html). This is a AWS Lambda function.

The [java version](java) is the original version, and also includes
- the chain_reps() function that finds one representative bitloop for each chain in a give powerset.
- output to .csv file, one per powerset.

The .json file in the python version is an aggregation of the .csv files for all powersets.