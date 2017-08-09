sudo docker run -ti --name emails -v $(pwd)/src:/src -p 8000:5000 -p 8001:5001 -p 8002:5002 --env-file /home/pablo/gitlab/fce/pablo/casa/emails emails
