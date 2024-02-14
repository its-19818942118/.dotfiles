#!/bin/bash

name=$1
compliment=$2

user=$(whoami)
date=$(date)
shell=$(which $SHELL)

echo "Good Morning $name"

sleep 2

echo "You are looking fresh today"

sleep 2

echo "You are the Best $compliment"

sleep 1

echo "Todays Date & Time is $date"

sleep 1

echo "You are Logged in as $user"

sleep 1

echo "You are using the $shell Shell"
