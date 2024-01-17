FROM fluent/fluentd:v1.16-debian-1
USER root

RUN gem uninstall elasticsearch elasticsearch-transport fluent-plugin-elasticsearch &&  \
    gem install elasticsearch -v 7.13.3 && gem install elasticsearch-transport -v 7.13.3 && \
    gem install fluent-plugin-elasticsearch -v 5.0.5

USER fluent





