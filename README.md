# Automatic-Ping


## Overview

This Python script monitors the ping metrics of a specified host for a given duration and logs the results into a CSV file. It periodically sends ping requests to the specified host, analyzes the results, and saves relevant metrics such as packets transmitted, received, lost, loss rate, as well as minimum, average, and maximum round-trip times (RTT).

## Features

- Periodically pings a specified host and logs the results into a CSV file.
- Captures metrics including packet transmission, reception, loss, loss rate, and RTT.
- Saves data in a structured format for easy analysis and monitoring.

## Usage

1. **Install Dependencies:**
   - Ensure you have Python 3.x installed on your system.
   - Install required libraries using `pip install pingparsing`.

2. **Run the Script:**
   - Modify the `host` and `duration` variables in the `main()` method to specify the target host and monitoring duration.
   - Execute the Python script using `python ping_metrics_logger.py`.




