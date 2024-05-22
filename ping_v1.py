import os
import time
import datetime
import csv
from pingparsing import PingParsing
from pingparsing import PingTransmitter

def ping_and_save_metrics(host, duration, output_file):
    # Initialize PingParsing instance
    ping_parser = PingParsing()

    # Calculate number of iterations based on duration
    num_iterations = int(duration.total_seconds())

    # Open CSV file for writing
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Destination', 'PacketTransmit', 'PacketReceive', 
                      'PacketLossCount', 'PacketLossRate', 'RTTMin', 'RTTAvg', 
                      'RTTMax', 'RTTMdev', 'PacketDuplicateCount', 'PacketDuplicateRate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Loop for each iteration
        for i in range(num_iterations):
            # Ping the host
            transmitter = PingTransmitter()
            transmitter.destination = host
            transmitter.count = 1  # Number of pings to send
            result = transmitter.ping()

            # Parse ping result
            parsed_result = ping_parser.parse(result)
            metrics = parsed_result.as_dict()

            # Extract desired values
            packet_transmit = metrics.get('packet_transmit')
            packet_receive = metrics.get('packet_receive')
            packet_loss_count = metrics.get('packet_loss_count')
            packet_loss_rate = metrics.get('packet_loss_rate')
            rtt_min = metrics.get('rtt_min')
            rtt_avg = metrics.get('rtt_avg')
            rtt_max = metrics.get('rtt_max')
            rtt_mdev = metrics.get('rtt_mdev')
            packet_duplicate_count = metrics.get('packet_duplicate_count')
            packet_duplicate_rate = metrics.get('packet_duplicate_rate')

            # Write data to CSV file
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow({'Timestamp': timestamp, 'Destination': host, 
                             'PacketTransmit': packet_transmit, 'PacketReceive': packet_receive, 
                             'PacketLossCount': packet_loss_count, 'PacketLossRate': packet_loss_rate, 
                             'RTTMin': rtt_min, 'RTTAvg': rtt_avg, 'RTTMax': rtt_max, 
                             'RTTMdev': rtt_mdev, 'PacketDuplicateCount': packet_duplicate_count, 
                             'PacketDuplicateRate': packet_duplicate_rate})

            # Wait for one second before the next ping
            time.sleep(1)

def main():
    host = "cmn61.stanford.edu"  # Modify with the destination host
    duration = datetime.timedelta(days=1)  # Total duration (one day)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Current date

    # Create a folder to save CSV files if it does not exist
    if not os.path.exists("ping_data"):
        os.makedirs("ping_data")

    # Define output file name
    output_file = f"ping_data/ping_metrics_{current_date}.csv"

    # Ping the host and save metrics to CSV
    ping_and_save_metrics(host, duration, output_file)

if __name__ == "__main__":
    main()
