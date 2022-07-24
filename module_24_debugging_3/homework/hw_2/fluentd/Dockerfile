FROM fluent/fluentd:v1.12.0-debian-1.0
USER root

RUN gem uninstall elasticsearch elasticsearch-transport fluent-plugin-elasticsearch &&  \
    gem install elasticsearch -v 7.13.3 && gem install elasticsearch-transport -v 7.13.3 && \
    gem install fluent-plugin-elasticsearch -v 5.0.5 && \
    gem install fluent-plugin-grok-parser -v 2.6.2

USER fluent





