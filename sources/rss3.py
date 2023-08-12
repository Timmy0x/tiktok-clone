import requests
import json

def get_rss3(amount=40):
    approved_addresses = ["0x0c74073f910a809e87d21830cbf86790fc8ca072"]
    base_url = "https://api.rss3.io/v1/notes"
    payload = {
        "limit": amount,
        "refresh": False,
        "include_poap": False,
        "ignore_contract": False,
        "count_only": False,
        "query_status": False,
        "address": approved_addresses,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    response = requests.post(base_url, json=payload, headers=headers).json().get("result")
    items = []
    for item in response:
        if item.get("actions")[0].get("metadata").get("media"):
            if "video/" in str(item.get("actions")[0].get("metadata").get("media")[0].get("mime_type")):
                items.append({
                    "date": item.get("created_at"),
                    "url": item.get("actions")[0].get("metadata").get("media")[0].get("address"),
                    "author": item.get("actions")[0].get("metadata").get("author")[1],
                    "description": item.get("actions")[0].get("metadata").get("body"),
                })
    return items