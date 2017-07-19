#!/bin/bash
ansible-playbook -vv ./dev_deploy.yml --private-key=/path/to/.ssh/key_name -u deploy -i ./hosts