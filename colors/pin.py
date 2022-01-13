import json
import sys

try:
    package = None
    file = sys.argv[1]

    with  open(file) as f:
        package = json.loads(f.read())
        if 'resolutions' in package:
            package['resolutions']['colors']="1.4.0"
        else:
            package['resolutions'] = {"colors":"1.4.0"}

    with open(file, "w") as f:
        f.write(json.dumps(package, indent=4))
except Exception as e:
    print("No-op:error {}".format(e))    
