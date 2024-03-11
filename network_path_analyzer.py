import subprocess
import argparse
import ipwhois
import re


class NetworkPathAnalyzer:
    """
    This class analyzes the network path using tracert and retrieves information about the hops.
    """

    def __init__(self):
        pass

    @classmethod
    def get_ip_addresses_and_asns_info(cls, destination: str) -> list[tuple[str, str, str, str]]:
        """
        This method uses tracert to get a list of IP addresses, ASNs, ISPs, and countries.

        Args:
            destination: The hostname or IP address to trace (str).

        Returns:
            A list of tuples containing IP addresses, ASNs, ISPs, and countries (list[tuple[str, str, str, str]]).
        """
        ip_info_list = []

        # Run tracert command and capture the output
        tracert_process: subprocess.Popen = subprocess.Popen(['tracert', destination], stdout=subprocess.PIPE)
        output, _ = tracert_process.communicate()

        # Decode the output from bytes to string
        output_str = output.decode('utf-8')

        # Loop through each line of the output (excluding the first line)
        for line in output_str.splitlines()[1:]:
            # Extract the IP address using regular expression (modify if needed)
            match: re.Match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if match:
                ip_address = match.group()

                try:
                    # Get ASN, ISP, and country information using ipwhois
                    obj: ipwhois.IPWhois = ipwhois.IPWhois(ip_address)
                    results = obj.lookup_rdap(depth=1)
                    asn = results['asn']
                    isp = results.get('asn_description', None)  # Handle potential absence
                    country = results.get('asn_country_code', None)  # Handle potential absence
                    ip_info_list.append((ip_address, asn, isp, country))
                except ipwhois.exceptions.IPDefinedError:
                    print("Error: IP address", ip_address, "is not defined in WHOIS database.")
                except Exception as e:
                    print(f"Error occurred while retrieving info for {ip_address}: {e}")

        return ip_info_list

    def run_analysis(self, destination: str) -> None:
        """
        This method executes the network path analysis and prints the results.

        Args:
            destination: The hostname or IP address to trace (str).
        """
        ip_asn_list: list[tuple[str, str, str, str]] = self.get_ip_addresses_and_asns_info(destination)

        if ip_asn_list:
            print("List of IP addresses and their information:")
            for ip, asn, isp, country in ip_asn_list:
                print(f"IP address: {ip}, ASN: {asn}, ISP: {isp}, Country: {country}")
        else:
            print("No IP addresses found in the tracert output.")


def main():
    # Define argument parser
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Get IP addresses and ASNs from tracert")
    parser.add_argument("destination", help="Hostname or IP address to trace", type=str)
    args: argparse.Namespace = parser.parse_args()

    # Create NetworkPathAnalyzer object
    analyzer: NetworkPathAnalyzer = NetworkPathAnalyzer()

    # Run network path analysis
    analyzer.run_analysis(args.destination)


if __name__ == "__main__":
    main()
