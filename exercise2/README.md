# Jenkins Plugin Installation

**Builds a docker container running jenkins with the list of plugins defined in `plugins.txt` pre-installed on the image**

This makes use of the script included with Jenkins for installing plugins and associated dependencies:

[https://github.com/jenkinsci/docker/blob/master/install-plugins.sh](https://github.com/jenkinsci/docker/blob/master/install-plugins.sh)

## Example Usage

`docker build -t jenkins-with-plugins .`

`docker run -p 8080:8080 -p 50000:50000 -v $(pwd)/jenkins_home:/var/jenkins_home jenkins-with-plugins`

One can then inspect the `jenkins_home/plugins` directory to see that the specified plugins and their dependencies have been installed - or head to [localhost:8080](http://localhost:8080) and see the same list
