#!/usr/bin/python3
"""import model"""

if __name__ == "__main__":
    import requests
    from sys import argv
    data = {"q": argv[1] if len(argv) > 1 else ""}
    request = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
