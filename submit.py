import json
import hmac
import hashlib
import datetime
import os
import requests

URL = "https://b12.io/apply/submission"
SECRET = b"hello-there-from-b12"

payload = {
    "timestamp": datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
    "name": "Oleh Siloch",
    "email": "olehsiloch3@gmail.com",
    "resume_link": "https://www.linkedin.com/in/oleh-siloch-7a68543a3",
    "repository_link": "https://github.com/YOUR_GITHUB_USERNAME/b12-application",
    "action_run_link": os.environ["GITHUB_RUN_URL"],
}

body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

sig = hmac.new(SECRET, body, hashlib.sha256).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={sig}",
}

resp = requests.post(URL, data=body, headers=headers)
resp.raise_for_status()
print(resp.json()["receipt"])
