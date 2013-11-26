Fabric File for Printing
========================

A short fabric-based application for letting people with access to my server
print local files from it over SSH.

Installation
------------

After cloning this repository, simply run `pip install -r requirements.txt`.

Usage
-----

To print the file `/home/some_user/blah.txt`, simply enter

    fab print2remote:/home/some_user/blah.txt

