import os
import sqlite3
import datetime
import random
import time

# Configuration
DB_NAME = "system_health.db"

def init_db():
    """Initialize SQLite database table for metrics."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            cpu_usage REAL NOT NULL,
            memory_usage REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def log_metric(cpu, memory, status):
    """Insert collected system metrics into database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO metrics (timestamp, cpu_usage, memory_usage, status)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, cpu, memory, status))
    conn.commit()
    conn.close()

def check_system_health():
    """Simulate checking server metrics and evaluating thresholds."""
    cpu_usage = round(random.uniform(15.0, 95.0), 2)
    memory_usage = round(random.uniform(40.0, 90.0), 2)
    
    # Determine alert threshold (e.g., CloudWatch SNS trigger scenario)
    if cpu_usage > 80.0 or memory_usage > 85.0:
        status = "WARNING"
        print(f"[ALERT] High resource load detected! CPU: {cpu_usage}%, MEM: {memory_usage}%")
    else:
        status = "HEALTHY"
        print(f"[OK] System Healthy. CPU: {cpu_usage}%, MEM: {memory_usage}%")
        
    log_metric(cpu_usage, memory_usage, status)

if __name__ == "__main__":
    print("Starting Cloud System Health Monitor...")
    init_db()
    
    # Run 5 simulated health check cycles
    for _ in range(5):
        check_system_health()
        time.sleep(1)
        
    print("\nHealth check routine complete. Metrics logged to database.")