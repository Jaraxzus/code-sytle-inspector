#!/bin/bash
celery -A csi.celery worker -l info
