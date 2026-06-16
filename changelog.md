# Changelog

## 2.0.0-beta.3

- moved manager checking logic into its own class
- implemented a new check in the list creation logic for empty lists
- implemented all the apt logic exceptuating the updating logic
- improved outputting logic to fix empty lists and handle no updates cases
- changed line splitting to use shlex

## 2.0.0-beta.2

- fully implemented PkgList for listing packages from managers
- reimplemented deduplication instead using PkgList instantiation as a check
- added type hints and docstrings to all functions
- added headers
- added unknown managers check

## 2.0.0-beta.1

- added argument parsing and help menu
- implemented part of apt manager
- implemented --version flag
- added deduplication (may add logging at some point, will require different method)

## 2.0.0-beta.0

- initial version
