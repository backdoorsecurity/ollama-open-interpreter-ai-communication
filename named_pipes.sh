#!/bin/bash
mkfifo /tmp/executioner
sleep 1
mkfifo /tmp/manager
sleep 1
chmod 666 /tmp/executioner
sleep 1
chmod 666 /tmp/manager
