FROM jenkinsci/jenkins

COPY ./plugins.txt /tmp/plugins.txt
RUN echo "specified plugins to be included:" && cat /tmp/plugins.txt
RUN /usr/local/bin/install-plugins.sh $(cat /tmp/plugins.txt | tr "\n" " ")
