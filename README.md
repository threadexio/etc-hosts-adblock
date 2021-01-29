# etc-hosts-adblock
Python script designed to fetch domains from a list and add them to /etc/hosts

## Instructions
1. Install the python requests module
```bash
pip install requests
or
pip3 install requests
```

2. Add more lists in `adlists.list` (Optional)

3. Run the script
```bash
./get_adblock.py
or
python get_adblock.py
```

4. Copy the newly created file to `/etc/hosts`

**NOTE:** This script makes a backup of your current `/etc/hosts` in `hosts.bak`

5. Flush your DNS cache
This can be done in numerous ways, just search on your search engine of choice: `how to flush the dns cache on [OS or distro name here]`
