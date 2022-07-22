FROM fluent/fluentd:v1.14.0-debian-1.0
USER root
RUN gem uninstall -I elasticsearch && gem install elasticsearch -v 7.13.1
RUN gem install fluent-plugin-elasticsearch
#RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.1.4"]
USER fluent





