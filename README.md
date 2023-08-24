# vagrant

## Purpose

A common ubuntu dev environment.

## Prerequisites

* Windows 10
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) ≥ v7.0.8
* [Vagrant](https://developer.hashicorp.com/vagrant/downloads) ≥ v2.3.7
* [vagrant-disksize](https://github.com/sprotheroe/vagrant-disksize)
```
vagrant plugin install vagrant-disksize
```
* [vagrant-timezone](https://github.com/tmatilai/vagrant-timezone)
```
vagrant plugin install vagrant-timezone
```

## Installation

1. Download/Clone this repository
2. Open an ```ADMINISTRATOR Terminal``` into the downloaded/cloned repository, where the ```Vagrantfile``` is located <br/>
3. Execute

```
vagrant up
```

## Expand vdi

```
sudo cfdisk
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
```

If necessary

```
sudo parted ---pretend-input-tty /dev/sda resizepart 3 100% 
sudo partx -u /dev/sda 
sudo pvresize /dev/sda3 
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```

## Documentation

* [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile)
* [Vagrantfile Settings](https://developer.hashicorp.com/vagrant/docs/vagrantfile/machine_settings)
* [Ansible Playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks.html)
* [Ansible Roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html)
