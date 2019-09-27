#!/bin/bash

echo "Should show all nodes in NotReady state..."
ansible master -i hosts -m shell -a 'kubectl get nodes' --become -K