# Ansible Nautobot Demo

![](https://github.com/jvanderaa/nautobot-ansible-import/workflows/CI/badge.svg)

## Nautobot

Nautobot is a fork from Nautobot 2.10 to take the capabilities even further in the network automation space. Take a look at the info on the [NTC home page](https://www.networktocode.com/nautobot/). The same features that have been part of Nautobot are still around and will evolve. If you want to take a test drive of Nautobot, take a look at [https://demo.nautobot.com](https://demo.nautobot.com).

## Most Recent Updates

I have moved all of the data that was previously configured to be added to Nautobot within the 00_setup_nautobot_devices.yml
file to be configured in the all.yml. If looking to bootstrap your Nautobot environment, this is the
main information that will need to get updated.  

**Important Note**
> This is **NOT** meant to be run constantly in your environment. Please do not use as such. This is
> a bootstrapping setup, to get you running. The intent of Nautobot is to become the Source of Truth
> for your environment. If all you are doing is constantly updating Nautobot from your devices, then
> the source of truth is the network device, not Nautobot. Please be working to get your environment
> to the state that you have a Source of Truth that is NOT your device.

## Start

To setup Nautobot, checkout https://nautobot.readthedocs.io
Setup an API Key in the upper right admin panel
Generate an environment of devices to use

## Requirements

1. Nautobot Installation
2. Docker Desktop on system
3. If running on Windows, you do not have `make`. The Makefile is just shortcuts to be used. Take a
look at the Makefile for the exact commands that replace the specific make commands.

## How to

1. Setup Nautobot (see the beginning)
2. Setup a new file named .env that contains information about your Nautobot environment for the container. See below for example config
3. Update your `group_vars/all.yml`,  `group_vars/` and `host_vars/` accordingly with credentials to connect to the devices, see below for example config
4. Create a container - `make build`
5. Enter the container - `make cli`
6. Setup Nautobot with executing `ansible-playbook 00_setup_nautobot_devices.yml`
7. Setup Devices Into Netbox `ansible-playbook 01_setup_devices.yml -i start_inventory` replace `start_inventory` with whatever your static inventory file is
8. Setup Interfaces using dynamic inventory `ansible-playbook 02_setup_interfaces.yml -i nautobot_inventory.yml`
9. Run the audit `ansible-playbook 03_audit_nautobot.yml -i nautobot_inventory.yml` where you have updated the information in the nautobot_inventory.yml file


### ENV File setup

```
NAUTOBOT_TOKEN=<Nautobot Key>
NAUTOBOT_URL=<URL of Nautobot>
```

### Group Vars, Host Vars

```yaml
---
ansible_user: <username>
ansible_password: <password>
ansible_network_os: <corresponding Ansible OS>
```

hostvars will only contain information overriding data points. In the example, the only thing set in the host vars
section is:

```yaml
---
rack_location: 41
```

## URLs

Helpful [URLs](./urls.md) have a few other links that may be helpful.
