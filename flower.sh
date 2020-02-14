#!/bin/bash

# http://localhost:5555/
celery flower --broker=redis://127.0.0.1:6379/2
