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
* **LEO Variant Merge**: Merges geometry and simultaneously creates a variant attribute for the "Copy to Points"-SOP .
* **LEO Connect Points Intersect**: Creates lines between nearby points which do not intersect with another geometry.
* **LEO Render Out**: Creates an object-level node which only renders the incoming geometry.

### OBJ:
* **LEO Render Out Child**: Object-level node created by LEO Render Out.

### MAT:

## HDA Naming Reference:
Follow this naming reference to have a consitent workflow!


File Name: [type]_[hdaName]_v[xxx].hda

  * *sop_variantMerge_v001.hda*

Operator Name: LEO::[hdaName]::[x]

  * *LEO::variantMerge::1*

Operator Label: LEO [Hda Name]

  * *LEO Variant Merge*

Version: x

  * *1*

Interactive - Shelf Tools - Context - Network Pane - [type]

  * *SOP*

Interactive - Shelf Tools - Context - Tab Submenu Path - LEO

  * *LEO*

## Installation:
Download or clone this repo and place it somewhere safe.

### Method 1: houdini.env
The houdini.env on Windows 10 should be located at c:\users\\[username]\Documents\houdini[version]

Add following to the env but change the "LEO" path to the downloaded directionary

```
LEO="E:/Projects/LEO_Tools"

HOUDINI_PATH=$LEO;&
```
