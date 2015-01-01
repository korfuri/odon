FROM ubuntu:trusty
EXPOSE 9001
CMD /etc/tor/run
RUN sh -c 'echo "deb http://deb.torproject.org/torproject.org trusty main" >> /etc/apt/sources.list && gpg --keyserver keys.gnupg.net --recv 886DDD89 && gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add - && apt-get update && apt-get install -y tor deb.torproject.org-keyring python python-pip screen && pip install stem && pip install flask'
USER debian-tor
COPY torcfg /etc/tor
