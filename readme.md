![FlaskMask logo](/FlaskMask.png)

This branch features a simple ansible deployment script. clone this repository and add a app folder next to the ansible folder. Running the ansible script will automatically copy the app folder to the server and run the docker-compose file inside app/docker on the server. A quick way to build a MVP.

## Getting started
Here you find instructions getting a devenvironment or autodeploying to server using ansible.

### Deploying to server
#### Requirements
- Ansible + ansible-playbook
- A server to deploy on

#### Instructions
1. Put the right host in the inventory file located in ´ansible/hosts´
2. Make sure you generate RSA keys for ssh ´ssh-keygen -t rsa -b 4096´
3. Run the initial server configurations in ansible folder ´run.sh initconfig´ - this will add sudo user, rsa keys and harden the server
4. Deploy the app to the server ´run.sh deploy´
5. If you need to run additional configs as sudo user use `run.sh config`

## LICENSE
MIT LICENSE

By Anders L. Hurum
