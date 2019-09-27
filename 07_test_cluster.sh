#!/bin/bash

echo "Should show all nodes in Ready state..."
ansible master -i hosts -m shell -a 'kubectl get nodes' --become -K