import sys
import requests
import json

def send_apdu(apdu_hex: str) -> str:
    """Send APDU data to the API and return the response."""
    url = "http://localhost:5000/apdu"
    
    try:
        response = requests.post(url, json={"data": apdu_hex})
        response.raise_for_status()  # Raise exception for non-200 status codes
        
        result = response.json()
        response_data = result.get("data", "")
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return ""

def main():
    print("APDU Exchange Tool - Enter hex data (or 'quit' to exit)")
    while True:
        try:
            # Get fresh input each time
            hex_input = input().strip()
            
            if hex_input.lower() in ['quit', 'exit', 'q']:
                print("Exiting...")
                break
                
            if not hex_input:
                print("Empty input, please try again")
                continue
                
            # Remove spaces from input
            hex_input = hex_input.replace(" ", "")
            
            try:
                # Validate hex format
                bytes.fromhex(hex_input)
            except ValueError as ve:
                print(f"Error: Invalid hex input - {ve}")
                continue
                
            response = send_apdu(hex_input)
            if response:
                print(f"=> {response}")
            
        except KeyboardInterrupt:
            print("\nInterrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
