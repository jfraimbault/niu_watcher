import os, sys
import tinytuya

device_id = os.environ["TUYA_DEVICE_ID"]
c = tinytuya.Cloud(
    apiRegion="eu",
    apiKey=os.environ["TUYA_ACCESS_ID"],
    apiSecret=os.environ["TUYA_ACCESS_SECRET"],
    apiDeviceID=device_id,
)

action = sys.argv[1] if len(sys.argv) > 1 else "status"

if action in ("on", "off"):
    r = c.sendcommand(device_id, {"commands": [{"code": "switch_1", "value": action == "on"}]})
    print(r)
    sys.exit(0 if r.get("success") else 1)
else:
    print(c.getstatus(device_id))
