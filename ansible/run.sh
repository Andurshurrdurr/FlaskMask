
if [ $1 = config ]
then
# To configure blank server, uncomment the following line:
  echo "Running server config!"
  ansible-playbook config.yml -i hosts --ask-pass
elif [ $1 = deploy ]
then
# If server is configured already, run the following line:
# First we delete the compiled python files
  echo "Deleting .pyc files"
  find ../app/ -name "*.pyc" -type f -delete
  echo "-- OK --"
  echo "Deploying app!"
  ansible-playbook deploy.yml -i hosts
else
  echo "Please a valid command."
fi
