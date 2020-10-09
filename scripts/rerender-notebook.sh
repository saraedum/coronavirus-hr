#!/bin/bash
set -e

cd "$(dirname "$0")"/..

# Rerender notebook.
jupyter nbconvert Koronavirus.ipynb --to notebook --inplace --execute

# Trust notebook so the plots show immediately.
jupyter trust Koronavirus.ipynb

# Rerender static HTML notebook
jupyter nbconvert Koronavirus.ipynb --to html --stdout --no-input > index.html
