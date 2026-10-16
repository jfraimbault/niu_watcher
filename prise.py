import os, sys
import tinytuya

device_id = os.environ.get("TUYA_DEVICE_ID", "").strip()
api_id = os.environ.get("TUYA_ACCESS_ID", "").strip()
api_secret = os.environ.get("TUYA_ACCESS_SECRET", "").strip()

if not (device_id and api_id and api_secret):
    sys.exit("Un des secrets est vide : vérifie leurs noms dans GitHub.")

c = tinytuya.Cloud(apiRegion="eu", apiKey=api_id,
                   apiSecret=api_secret, apiDeviceID=device_id)

action = (sys.argv[1] if len(sys.argv) > 1 else "status").lower()

if action in ("on", "true"):
    value = True
elif action in ("off", "false"):
    value = False
else:
    print(c.getstatus(device_id))
    sys.exit(0)

r = c.sendcommand(device_id, {"commands": [{"code": "switch_1", "value": value}]})
print(r)
sys.exit(0 if r.get("success") else 1)
