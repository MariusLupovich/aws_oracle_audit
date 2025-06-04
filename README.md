# 📦 Cloud Audit & Reporting for Oracle Backups (Simulated)

This project demonstrates how an Oracle DBA can build a cloud-native backup audit system using AWS services. It simulates backup log processing and stores audit summaries for reporting.

## 🔧 Technologies Used
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- AWS SNS (optional)
- Amazon Athena (optional)
- Python & Boto3
- Bash

## 🧱 Architecture
```
User Uploads Log
       ↓
  [Amazon S3]  ←─────── sample_logs/*.json
       ↓ Trigger
  [AWS Lambda]  → Parses JSON → [DynamoDB Table]
       ↓
   (Optional: send alerts via SNS / query via Athena)
```

## 🚀 Setup Instructions

1. Create S3 bucket and DynamoDB table
2. Deploy Lambda function
3. Upload logs using provided script
4. Connect Lambda trigger in S3
5. (Optional) Setup Athena and SNS

## 📁 Output Example
```json
{
  "BackupId": "bk_20250601_001",
  "Status": "SUCCESS",
  "SizeMB": 5421,
  "Timestamp": "2025-06-01T02:30:00Z"
}
```
# Thats all folks