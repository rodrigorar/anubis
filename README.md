# Olisipo

[![Olisipo Password Manager](https://github.com/rodrigorar/olisipo/actions/workflows/python-app.yml/badge.svg)](https://github.com/rodrigorar/olisipo/actions/workflows/python-app.yml)

## Description

A simple local terminal based secrets manager.

## Commands

### `add <entry_key> <entry_value>`

Add secret with **key** \<entry_key\> and **value** \<entry_value\> to the
existing secrets datastore or **replace** and existing secret with the new value. 

### `get <entry_key>`

Get secret from secrets database with **key** \<entry_key\> and return its
value or nothing in case the entry does not exist. 

### `list`

List all existing secrets in the secrets datastore by listing their keys. 

### `remove <entry_key>`

Remove secret from secrets datastore with **key** \<entry_key\> if the user can
provide the proper secret, otherwise do nothing. 

### `help`

Show help menu

### `q`

Exit the application

## Contributing

If you wish to contribute to this project, fork the repository, add any new feature 
you want and create a PR for this repo, and i'll check it out! :) 
