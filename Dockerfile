FROM kbase/kbase:sdkbase.latest
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

# RUN apt-get update

RUN . /kb/dev_container/user-env.sh && cd /kb/dev_container/modules && \
   rm -rf jars && git clone https://github.com/rsutormin/jars && \
   rm -rf kb_sdk && git clone https://github.com/rsutormin/kb_sdk -b develop && \
   cd /kb/dev_container/modules/jars && make deploy && \
   cd /kb/dev_container/modules/kb_sdk && make && make deploy
# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
