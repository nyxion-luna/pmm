# update

## What is this?

update is a command that will help you update without juggling all your different package managers, eventually forgetting one.

## Why use this instead of other options?

update shows the packages that are going to be installed. it checks all the package managers that it supports, and if it's installed, it gets the upgradable packages, their current and new version, and displays it all in a list.

## Which package managers are supported?

Currently, only one package manager is supported:

- apt

The following package managers will eventually be implemented:

- all (detects which are installed)
- npm
- flatpak
- snap
- dnf
- pacman
- brew
- pip
- npm
- cargo
- gem
- nix

## Roadmap

There is a planned rebrand to 'pmm' but there is no specified date this rebrand will happen.

### v1

First working version (hopefully) without major bugs.
This version will however only support apt. I want to do that python rewrite asap.

v1.x -> More managers if I'm too lazy to rewrite this thing tho.

### v2

Rewrite to python with all features and managers in v1. Will be adding more.

### v3

Managing individual packages per manager (not autosearch, you have to input manager AND package name fully). This might be individual package updating or full on installation and removal of packages, depends on my willingness to write it at the time.

### v4

Automatic package searching
v3 and v4 are things I will try to implement. No promises.
