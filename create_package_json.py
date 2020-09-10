import json
import os

def run():
	path = os.getcwd().replace("\\","/")

	content = {
				"recommends": "houdini_version >= '18.0'",
				"env":[
						{"LEO": path},
						{
							"PYTHONPATH": "$LEO/scripts/python",
							"method": "append"
						}
					],
				"path": "$LEO"

				}


	with open("LEOTools_package.json", "w") as f:
		json.dump(content,f,indent=4)

if __name__ == "__main__":
	run()
					


