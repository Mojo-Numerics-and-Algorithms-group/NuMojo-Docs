# NuMojo-Docs

Documentation and Base for documentation website for NuMojo.

## How to run checks and change code

Clone this repository

`pip install mdutils mkdocs mkdocs-material`

cd into NuMojo and run `mkdocs serve` in the terminal.

## Generating MD files from Mojo docs jsons

In the folder containing the NuMojo package run `mojo doc numojo/ -o docs.json` then move docs.json into the directory that you cloned NuMojo-Docs into. Then run docs.py, and it will generate the documentation and put it in the correct place.
