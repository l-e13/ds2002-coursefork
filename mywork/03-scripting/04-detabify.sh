#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "This script converts a TSV into a CSV";
  echo "Append the input file name and then the output file name";
fi

# This will turn TSV into CSV

/usr/bin/tr '\t' ',' < $1 > $2
