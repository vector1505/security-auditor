<<<<<<< HEAD
# Security Analysis API

A Django-based API service that provides security analysis capabilities including SSL certificate analysis, security headers checking, malware/phishing detection, and network scanning.

## Features

- SSL certificate analysis (SSL Labs)
- Security headers validation
- Malware and phishing detection (Google Safe Browsing/VirusTotal)
- Network scanning (Shodan)
- DNS security checks (DNSSEC, SPF, DMARC)
- Optional vulnerability scanning (NVD/WPScan)

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/v1/ssl-analysis/` - SSL certificate analysis
- `/api/v1/security-headers/` - Security headers checking
- `/api/v1/malware-check/` - Malware/phishing detection
- `/api/v1/network-scan/` - Network scanning
- `/api/v1/dns-check/` - DNS security checks
=======
# security-auditor

An AI powered solution for all your web safety needs

The team includes:

Mentors: 
1. Mohit Talgotra
2. Nidhi Karva

Team Init:2winit 

1. Vinayak Joshi - Tech
2. Ramish Faraz - Management
3. Tarun Ram - Management
4. Gayathri S Nair - Management
5. Lakshay Gupta - Design
6. Ashwini G - Design
>>>>>>> 49226bbed6b9a204e037341ea6df5edc68b9deab
