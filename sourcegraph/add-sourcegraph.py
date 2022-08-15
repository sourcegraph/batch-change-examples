import sys
import json

if __name__ == "__main__":
    try:
        fileList = map(str, sys.argv[1].strip('[]').split(','))
        try:
            for filePath in fileList:
                f = open(filePath)
                data = json.load(f)
                if "recommendations" in data:
                    if not("sourcegraph.sourcegraph" in data["recommendations"]):
                        data["recommendations"] = data["recommendations"] + ["sourcegraph.sourcegraph"]
                else:
                    data["recommendations"] = ["sourcegraph.sourcegraph"]
                f.close()
                with open(filePath, 'w') as outfile:
                    json.dump(data, outfile, indent=2)
        except Exception as error:
            print(error)
    except:
        print("Didn't find any files. Exiting.")        
        



