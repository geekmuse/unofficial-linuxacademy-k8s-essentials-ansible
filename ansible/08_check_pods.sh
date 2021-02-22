#!/bin/bash

echo "Should see n 'flannel' pods in state 'Running' where n = number of nodes you set up..."
ansible master -i hosts -m shell -a 'kubectl get pods -n kube-system' --become -K