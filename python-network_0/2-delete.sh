#!/bin/bash
# Script that sends a DELETE request to URL passed as the first argument
curl -sX "DELETE" "$1"
