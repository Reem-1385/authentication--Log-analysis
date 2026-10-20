
Authentication Log Analysis and Suspicious Login Detection
Project Overview
This project analyzes sample authentication logs to identify repeated failed login attempts and flag potentially suspicious IP addresses.

Objectives
Analyze authentication log data using Python.

Count failed login attempts by source IP address.

Identify IP addresses with five or more failed login attempts.

Generate a CSV report containing the analysis results.

Tools and Technologies
Python 3

Pandas

Google Colab

GitHub

CSV datasets

Project Files
authentication_log_analysis.py — Python script for log analysis.

authentication_logs.csv — Sample authentication log dataset.

suspicious_logins.csv — Analysis results.

Detection Logic
The script groups failed login attempts by source IP address. An IP address with five or more failed attempts is flagged as Suspicious for further review.

Sample Results
The sample dataset contains seven login attempts: two successful and five failed attempts. The analysis flags one IP address for review.

How to Run
Install Python 3 and Pandas.

Place authentication_logs.csv in the same directory as the Python script.

Run the script using Python.

Review the generated suspicious_logins.csv file.

Disclaimer
This project uses synthetic sample data for educational purposes. A suspicious classification is an alert for further investigation and does not confirm malicious activity.

