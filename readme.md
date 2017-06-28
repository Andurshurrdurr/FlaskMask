# FlaskMask

This repository contains boilerplate code for quickly setting up and deploying a containerized flask webapplication. This repo will be purposefully designed for lean dev, experimentation and hackathons.

## Getting started
Here you find instructions getting a devenvironment or autodeploying to server using ansible.

### Development environment
#### Using vagrant:
[This is still experimental and not tested]

##### Requirements
- Virtualbox
- Vagrant

##### Instructions
1. Move to the app directory
2. Run vagrant ´vagrant up´
3. SSH into vagrant vm ´vagrant ssh´
4. Once in you will find the synced folder at ´cd /vagrant´
5. Run the application ´python main.py´

#### Using virtualenv
[Also quite experimental]

##### Requirements
- python
- virutalenv
- pip

##### Instructions
1. Move terminal to app directory ´cd app/app´
2. Create a virtual environment ´virtualenv venv´
3. Initiailize a virtualenv session ´source venv/bin/activate´
4. Install the requirements ´pip install -r requirements.txt´
5. There might be some packages which must be installed globally using sudo - pip should tell you
6. Run the app ´python main.py´

### Deploying to server
#### Requirements
- Ansible + ansible-playbook
- A server to deploy on

#### Instructions
1. Put the right host in the inventory file located in ´ansible/hosts´
2. Make sure you generate RSA keys for ssh ´ssh-keygen -t rsa -b 4096´
3. Run the server configurations in ansible folder ´run.sh config´
4. Deploy the app to the server ´run.sh deploy´
5. For now you need to log into the server and run docker-compose up

## Features
- Ansible playbook autodeploy
- Docker for containerization, docker-compose for orchestration
- Python and flask
- MySQL RDB
- Containers which handle node communication using different protocols

## LICENSE
MIT LICENSE

By Anders L. Hurum
