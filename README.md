# Linux Academy - Kubernetes Essentials

Sets up a k8s cluster according to Linux Academy's "Kubernetes Essentials" course, using Ansible.

## Setup

```bash
$ pip3 install -r requirements.txt
$ cp conf.yml.example conf.yml
```

## To Use

### Setup

Replace values in `conf.yml` as appropriate.

```bash
$ python3 build_hosts_file.py
```

### Test Ansible

```bash
$ ansible all -i hosts -m ping
```

### Run It

```bash
$ ansible-playbook all -i hosts 01_install_docker.yml [-K]
$ ansible-playbook master -i hosts 02_setup_kubeadm.yml [-K]
$ ansible-playbook nodes -i hosts 03_cluser_join.yml [-K]
$ ./04_test_cluster.sh
$ ansible-playbook all -i hosts 05_networking.yml [-K]
$ ansible-playbook master -i hosts 06_setup_flannel.yml [-K]
$ ./07_test_cluster.sh
$ ./08_check_pods.sh
```