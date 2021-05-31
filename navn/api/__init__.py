from flask import Blueprint
from . import netbox

bp = Blueprint("api", __name__, url_prefix="/api")
bp.register_blueprint(netbox.bp)
