# To configure blank server, uncomment the following line:
#ansible-playbook site.yml -i hosts --ask-pass

# If server is configured already, run the following line:
ansible-playbook site.yml -i hosts -K
