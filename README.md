Fabric File for Printing
========================

A short fabric-based application for letting people with access to my server
print local files from it over SSH.

Installation
------------

After cloning this repository, simply run `pip install -r requirements.txt`.
Run `fab setup_settings` to generate a custom settings file (a custom settings
file is used to minimize disruption in case I push a new settings file).
In the custom settings file (`custom_settings.py`), change host and user as appropriate.

Usage
-----

To print the file `/home/some_user/blah.txt`, simply enter

    fab print2remote:/home/some_user/blah.txt

