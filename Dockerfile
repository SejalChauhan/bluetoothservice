# Bluetooth Starter
#
# Scans for Bluetooth devices and displays the results via a web server.

# Specify the base image.
FROM ubuntu:latest

# Install dependencies.  You can add additional packages here following the example.

RUN apt-get update
RUN apt-get install -y \
    python python-pip python-dev build-essential wget supervisor

# Install files required by the chute.
#
# ADD <path_inside_repository> <path_inside_container>
#
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY chute /app
WORKDIR /app
RUN pip install -r requirements.txt

# Make the web server's port available outside the container.  We will also
# need to configure port binding in the chute configuration.
#
# EXPOSE <port_inside_container>
#
EXPOSE 24180

# This is the command that will be run inside the container.  It can be a bash
# script that runs other commands, a python script, a compiled binary, etc.
ENTRYPOINT ["python"]
CMD ["app.py"]
CMD ["/usr/bin/supervisord"]
