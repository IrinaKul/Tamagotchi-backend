import flask_praetorian

from flask import request, redirect
from flask_accepts import accepts, responds
from flask_restx import Resource, Namespace

applinks_ns = Namespace('.well-known')


@applinks_ns.route("/assetlinks.json")
class AppLinksResource(Resource):
    def get(self):
        if request.MOBILE:
            return redirect('https://drive.google.com/file/d/1wzsl152Nr9HBctG65mMoBuMDk3yCyMT6/view')
        return [{
            "relation": ["delegate_permission/common.handle_all_urls"],
            "target": {
                "namespace": "android_app",
                "package_name": "ru.vsu.flutter_tamagotchi_app",
                "sha256_cert_fingerprints":
                    ["20:C1:23:71:58:2C:43:66:E2:93:D3:2E:AF:C5:95:C0:B2:9B:55:4C:64:96:97:30:7A:B2:B5:1C:EF:8B:1C:A4"]
            }
        },
            {
                "relation": ["delegate_permission/common.handle_all_urls"],
                "target": {
                    "namespace": "android_app",
                    "package_name": "ru.vsu.flutter_tamagotchi_app",
                    "sha256_cert_fingerprints":
                        [
                            "20:C1:23:71:58:2C:43:66:E2:93:D3:2E:AF:C5:95:C0:B2:9B:55:4C:64:96:97:30:7A:B2:B5:1C:EF:8B:1C:A4"]
                }
            }]
