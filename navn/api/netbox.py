import json
from flask import request, Blueprint
from pprint import pprint as pp
from .helpers import enforce_login

bp = Blueprint("netbox", __name__, url_prefix="/netbox")


@bp.route("/", methods=["POST"])
@enforce_login
def netbox_handler():
    """
    This will handle the callbacks from Netbox to process the IP address
    changes.

    The data is only posted.
    """
    data = json.loads(request.data)
    event = data["event"]
    ip_address = data["data"]["address"]
    pre = data["snapshots"]["prechange"]
    post = data["snapshots"]["postchange"]
    print(f"event: {event}")
    print(f"ip address: {ip_address}")

    if event == "updated":
        important_keys = ["custom_fields.CNAME", "dns_name", "address"]
        changes = {}
        for key in important_keys:
            if "." in key:
                key = key.split(".")
                if pre[key[0]][key[1]] != post[key[0]][key[1]]:
                    changes[".".join(key)] = [pre[key[0]][key[1]], post[key[0]][key[1]]]
                continue
            if pre[key] != post[key]:
                changes[key] = [pre[key], post[key]]

        if "dns_name" in changes or "address" in changes:
            print("update A record")
            print("update PTR record")

        if "custom_fields.CNAME" in changes:
            print("figure out diff")
            print("update records")
    elif event == "deleted":
        to_delete = data["snapshots"]["prechange"]
        print(f"delete {to_delete['dns_name']}")
        print(f"delete {to_delete['custom_fields']['CNAME']}")
    elif event == "created":
        to_add = data["snapshots"]["postchange"]
        print(f"add {to_add['dns_name']}")
        print(f"add {to_add['custom_fields']['CNAME']}")
    return "None."


@bp.route("/", methods=["GET"])
def netbox_get():
    return "You need to post data!"
