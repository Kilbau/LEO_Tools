# LEO_Tools (Beta):
A collection of HDAs for SideFX Houdini.
I'll upload them whenever I created a new one for my projects.

They are made with Houdini 18(.5) **Indie** and should only work with Indie, Apprentice or Educational.

Also I'll add some useful code to the useful folder whenever I encounter something cool.
Newer tools are made for Python 3 but should still work with Python 2 builds of Houdini.

## List of current HDAs:
All nodes are documentated via the houdini documentation. To view the documentation press F1 or the questionmark-icon in the parameters.

### SHELF TOOLS:
* **LEO Random Ramp**: Updates or adjusts ramp parameters by random values to generate more interesting results.

### SOP:
* **LEO Color Ramp Picker**: Allows the interactive creation of a color ramp in the viewport. [Demo Video](https://vimeo.com/448546910)
* **LEO Group Intersecting Object**: Generates a group based on the intersection with another geometry.
* **LEO Variant Merge**: Merges geometry and simultaneously creates a variant attribute for the "Copy to Points"-SOP. [Demo Video](https://vimeo.com/448293988)
* **LEO Connect Points Intersect**: Creates lines between nearby points which do not intersect with another geometry.
* **LEO Object Render**: Creates an object-level node which only renders the incoming geometry.
* **LEO Attribute Split**: Splits an incoming geometry based on an attribute.
* **LEO Weighted Random**: Creates an random attribute based on weighted inputs. [Demo Video](https://vimeo.com/448293988)
* **LEO Lattice**: Easily place a lattice deformer anywhere on a mesh. [Demo Video](https://vimeo.com/535531223)
* **LEO Linked Subnets**: Connects subnets together to copy nodes and parameters. [Demo Video](https://vimeo.com/618260092) or [More Information](https://www.sidefx.com/forum/topic/80497/#post-348519)

### OBJ:
* **LEO Object Render Child**: Object-level node created by LEO Object Render.

### MAT:

## Installation:
Download or clone this repo and place it somewhere safe.

### Method 1: houdini.env
The houdini.env on Windows 10 should be located at 

```c:/users/[username]/Documents/houdini[version]```

Add following to the env but change the "LEO" path to the downloaded directionary

Add the path to both the ```HOUDINI_PATH``` as well as the ```PYTHONPATH```

Example houdini.env file
```
LEO = "E:/Projects/LEO_Tools"

HOUDINI_PATH = $LEO;&
PYTHONPATH = "$LEO/scripts/python;&"
```

### Method 2: Plugin / Packages
***Requires Houdini 17.5+***

Put the LEOTools_package.json file into the packages folder. 

It should be located here on Windows:

```c:/users/[username]/Documents/houdini[version]/packages```

On Linux:

```~Library/Preferences/Houdini```

Finally update following line to match your downloaded directionary

```"LEO": "D:/Resources/HDA/LEO_Tools"``` 

***NOTE:***
If you have Python installed on your system you can run the included ```create_package_json.py``` file.
This will create a new LEOTools_package.json with the path to the current directionary.
### Display Shelf ###

Add the "LEO Tools" shelf by clicking on the plus by the shelves
"+" -> "Shelves" -> "LEO Tools"
