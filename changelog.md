# Changelog

## 2.0.0-beta.4

- finished the updating logic for apt
- implemented --dry-run --no-sudo and --yes flags
- made the package list per manager no longer a global variable
- clarified the info for the --dry-run flag
- implemented a sudo keepalive to avoid running into extra sudo checks
- made the default state of _has_updates False
- added a header function
- fixed PkgList.output() not printing before returning
- removed the BaseManager.verify_sudo() method in favour of the background keepalive
- added check for whether any manager ended up in instances
- added a default choice to the update query

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
