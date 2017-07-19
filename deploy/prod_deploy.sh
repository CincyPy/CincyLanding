#!/bin/bash
ansible-playbook -vv ./deploy.yml --private-key=/path/to/.ssh/ssh_key_name -u deploy -i ./hosts