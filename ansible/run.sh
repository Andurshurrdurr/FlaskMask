
if [ $1 = config ]
then
# To configure blank server, uncomment the following line:
  echo "Running server config!"
  ansible-playbook config.yml -i hosts --ask-pass
elif [ $1 = deploy ]
then
# If server is configured already, run the following line:
  echo "Deploying app!"
  ansible-playbook deploy.yml -i hosts -K
else
  echo "Please a valid command."
fi
