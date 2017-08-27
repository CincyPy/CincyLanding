#!/bin/bash
ansible-playbook -vv ./create_superuser.yml --private-key=/path/to/.ssh/key_name -u root -i ./hosts
