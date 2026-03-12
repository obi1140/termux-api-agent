import requests
import sys

def fetch_crypto_price(token):
    """Fetches the current USD price of a given cryptocurrency."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
    
    try:
        # The agent makes a request to the external API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Parse the JSON response
        if token in data:
            price = data[token]['usd']
            print(f"[+] SUCCESS: The current price of {token.capitalize()} is ${price:,.2f}")
        else:
            print(f"[-] ERROR: Token '{token}' not found. Try 'bitcoin' or 'ethereum'.")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] API ERROR: Could not connect to the data source.\nDetails: {e}")

if __name__ == "__main__":
    print("--- Minimal Crypto CLI Agent ---")
    
    # Allows the user to pass a token name directly in the command line
    if len(sys.argv) > 1:
        target_token = sys.argv[1].lower()
        fetch_crypto_price(target_token)
    else:
        print("Usage: python agent.py <token_name>")
        print("Example: python agent.py solana")
