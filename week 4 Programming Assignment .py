import multiprocessing

# Function to search for IP addresses in a file and return the matches
def search_ip(file_path, ip_list):
    with open(file_path, 'r') as f:
        ips = set(f.read().splitlines())
    matches = ips.intersection(ip_list)
    return matches

if __name__ == '__main__':
    multiprocessing.freeze_support()

    # Read in the evidence file and extract the IP addresses
    with open('evidence.txt', 'r') as f:
        evidence_ips = set(f.read().splitlines())

    # Create a pool of processes to search for the IP addresses in parallel
    pool = multiprocessing.Pool(processes=3)

    # Run the IP address search on each threat file in parallel
    results = [pool.apply_async(search_ip, args=(f'threat_{i}.txt', evidence_ips)) for i in range(1, 4)]

    # Get the results and combine the matched IP addresses from each file
    matched_ips = set()
    for result in results:
        matched_ips.update(result.get())

    # Print the matched IP addresses
    print(f'Matched IP addresses: {matched_ips}')

    
**************************************************************************************************************************
To run this code, save the code in a file named "investigator_toolkit.py" and also save the following files in the same directory as the script:

"evidence.txt": A file containing a list of IP addresses, one per line.
"threat_1.txt": A file containing a list of threat IP addresses, one per line.
"threat_2.txt": A file containing a list of threat IP addresses, one per line.
"threat_3.txt": A file containing a list of threat IP addresses, one per line.

Then, open a terminal or command prompt in the directory where the files are saved and run the following command: *** python investigator_toolkit.py ***

The output will be displayed in the terminal or command prompt.
