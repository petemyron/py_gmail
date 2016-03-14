# Send an email through Gmail
#
# docker run --rm -it \
#   --dns 8.8.8.8 \
#   petemyron/py_gmail \
#   python send_gmail.py \
#   -u email@domain.com \
#   -p mypassword \
#   -t otheremail@domain.com \
#   -s "oh haii" \
#   -b "this is only a test"

# Note: adapted from Michael J. Mitchell's <michael@mitchtech.net> py_gmail


FROM python:2-alpine

MAINTAINER Pete Myron <pete.myron@gmail.com>

COPY ./send_gmail.py /send_gmail.py

CMD ["python", "/send_gmail.py"]