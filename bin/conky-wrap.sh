#!/usr/bin/env bash
cd $1
echo "{ \"version\": 1 } ["
exec conky -c $1/conkyrc
