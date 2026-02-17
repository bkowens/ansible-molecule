# ansible-molecule

An Ansible role that installs and configures nginx with a Hello World page, tested with Molecule using Docker containers.

## Prerequisites

- Python 3.10+
- Docker

Ensure your user is in the `docker` group:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

## Setup

Clone the repository and create a virtual environment:

```bash
git clone git@github.com:bkowens/ansible-molecule.git
cd ansible-molecule
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

Run the full Molecule test lifecycle (create container, converge, verify, destroy):

```bash
molecule test
```

Individual steps can be run separately:

```bash
molecule create      # Create the Docker container
molecule converge    # Run the Ansible playbook
molecule verify      # Run TestInfra tests
molecule destroy     # Tear down the container
```

## What Gets Tested

The TestInfra tests validate:

- nginx package is installed
- nginx service is running and enabled
- Port 80 is listening
- The default page returns "Hello World"

## Role Variables

| Variable | Default | Description |
|---|---|---|
| `nginx_hello_message` | `Hello World` | Message displayed on the landing page |

## Using the Role

Add this role to a playbook:

```yaml
- hosts: webservers
  become: true
  roles:
    - ansible-molecule
```
