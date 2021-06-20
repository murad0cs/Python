FROM python 							# install Flask in the container
                          # container will need the website folders. COPY them under /home/myapp inside the docker container
COPY  myapp.py /home/application
EXPOSE 8080				# EXPOSE port 8080 to be used by the webserver
CMD python3 /home/application/application.py	# execute the python script
