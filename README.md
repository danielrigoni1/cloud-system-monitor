# Cloud & Database Health Monitor

A lightweight Python service that collects system metrics, evaluates resource thresholds, and records audit logs into a SQL database. Designed to demonstrate backend automation, database interactions, and alert triggering concepts similar to cloud monitoring tools (e.g., AWS CloudWatch).

## Features
- **Automated Metric Collection:** Tracks simulated CPU and Memory utilization.
- **SQL Persistence:** Automatically initializes database schema and logs entries with ISO timestamps.
- **Alert Logic:** Evaluates system thresholds to trigger high-resource load warnings.

## Tech Stack
- **Language:** Python 3
- **Database:** SQLite / SQL
- **Concepts:** Monitoring, Automation, Incident Logging

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/daniel-rigoni/cloud-system-monitor.git](https://github.com/daniel-rigoni/cloud-system-monitor.git)
   cd cloud-system-monitor
