#!/bin/bash
name=""
for var in "${@:4}"
do
	name=${name}$var"."
done
echo $name
