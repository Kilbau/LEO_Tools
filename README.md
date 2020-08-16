# LEO_Tools:
A collection of HDAs for SideFX Houdini.
I'll upload them whenever I created a new one for my projects.

They are made with Houdini 18 **Indie** and should only work with Indie, Apprentice or Educational.

Also I'll add some useful code to the useful folder whenever I encounter something cool.

## List of current HDAs:
All nodes are documentated via the houdini documentation. To view the documentation press F1 or the questionmark-icon in the parameters.

### SCRIPTS:

### SOP:
* **LEO Color Ramp Picker**: Allows the interactive creation of a color ramp in the viewport.
* **LEO Group Intersecting Object**: Generates a group based on the intersection with another geometry.
* **LEO Variant Merge**: Merges geometry and simultaneously creates a variant attribute for the "Copy to Points"-SOP. [Demo Video](https://vimeo.com/448293988)
* **LEO Connect Points Intersect**: Creates lines between nearby points which do not intersect with another geometry.
* **LEO Render Out**: Creates an object-level node which only renders the incoming geometry.
* **LEO Attribute Split**: Splits an incoming geometry based on an attribute.
* **LEO Weighted Random**: Creates an random attribute based on weighted inputs. [Demo Video](https://vimeo.com/448293988)

### OBJ:
* **LEO Render Out Child**: Object-level node created by LEO Render Out.

### MAT:

## Installation:
Download or clone this repo and place it somewhere safe.

### Method 1: houdini.env
The houdini.env on Windows 10 should be located at c:\users\\[username]\Documents\houdini[version]

Add following to the env but change the "LEO" path to the downloaded directionary

```
LEO="E:/Projects/LEO_Tools"

HOUDINI_PATH=$LEO;&
```
