#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: $0 <bucket-name>"
  exit 1
fi

aws s3 cp sample_logs/backup_log_2025_06_01.json s3://$1/
