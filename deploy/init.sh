#!/bin/bash
ansible-playbook -vv ./init_config.yml --private-key=/path/to/.ssh/key_name -u root -i ./hosts
