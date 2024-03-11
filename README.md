# Network-Path-Analyzer
### Network Path Analyzer - Trace Route with IP Information

This Python program acts as a network path analyzer, combining the functionality of tracert with the power of WHOIS lookups. It helps you understand the route packets take to reach a specific destination on the internet and provides additional information about the encountered hops.

### What it Does:
- Traces Network Path: Leverages the tracert command to trace the route to a hostname or IP address, revealing the sequence of hops (intermediate network devices) packets traverse.
- Gathers IP Information: Retrieves details about each hop (if available), including:
  - IP Address: The numerical address of the hop.
  - ASN (Autonomous System Number): A unique identifier for the network responsible for the hop.
  - ISP (Internet Service Provider): (if available) The company providing internet access at that hop.
  - Country: (if available) The country where the hop is located.
- Utilizes ipwhois Library: Queries WHOIS databases to obtain this extended information beyond the basic IP address.

### Use Cases:
- Network Troubleshooting: Diagnose network connectivity issues by analyzing the path and identifying potential bottlenecks or interruptions.
- Security Analysis: Gain insights into the routing of your internet traffic and the entities involved.
- Network Research: Explore the structure of the internet and understand how data travels geographically.


### How to Use:
Prerequisites:
  - Python 3 installed (https://www.python.org/downloads/)
  - ipwhois library installed using pip install ipwhois
### Running the Script:
1. Save the program as network_path_analyzer.py.
2. Open a terminal and navigate to the directory containing the script.
3. Execute the script with the desired hostname or IP address as an argument:
```Bash
python network_path_analyzer.py <hostname_or_ip_address>
```
Replace <hostname_or_ip_address> with the target you want to trace (e.g., python network_path_analyzer.py www.google.com).

### Example Output:

The program will display a list of hops along with their corresponding IP addresses, ASNs, ISPs (if available), and countries (if available). Here's an example:
```Bash
List of IP addresses and their information:
IP address: 192.168.1.1, ASN: None, ISP: None, Country: None
IP address: 8.8.8.8, ASN: AS15169, ISP: Google Public DNS, Country: None
IP address: 216.58.217.206, ASN: AS16503, ISP: Level 3 Communications, Country: United States
```
### Further Notes:
- The program handles potential errors during information retrieval and gracefully reports them.
- The availability of ISP and country information depends on the WHOIS database entries for the respective ASNs.

This program offers a valuable tool for network analysis and exploration, providing a comprehensive view of the network path and the entities involved in internet communication.
