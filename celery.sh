#!/bin/bash

celery -A starter_service worker -l info -P eventlet
