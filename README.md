# LEO_Tools:
A collection of HDAs for SideFX Houdini.
I'll upload them whenever I created a new one for my projects.

They are made with Houdini 18 **Indie** and should only work with Indie, Apprentice or Educational.

Also I'll add some useful code to the useful folder whenever I encounter something cool.

## List of current HDAs:
### SOP:
* **variantMerge**: Merges Geometry and adds a variant attribute to be used with the H18 "copy to points"-SOP.
* **connectPointsIntersect**: Similar to connect adjacent pieces (connection type "adjacent points") but it doesn't create lines between points if the lines would intersect with another geometry.  
  **NOTE:** If you are using the same geometry for points and the intersection then you might have to push the input points a tiny bit along their normals. Otherwise they might intersect with themselves and don't create lines.
* **colorRampPicker**: Remaps an attribute to a color using images. The colors are interactively picked inside the viewport. (Requires H18+)
* **groupIntersectingObject**: Creates a group based on the intersection of two objects. The group is also expanded to contain the whole connected geometry.
* **renderOut**: Creates object-level RENDER_* nodes that is connected to the renderOut sop.
### OBJ:
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

#### WIP SOPS ####
* **alignPoint**: Align Geometry to another Geometry based on a selected Point (currently only one point for Source and Target supported) 
* **distribute**: Easy art-directable scattering (maybe includes support for viewerstates)
* **simpleGrass**: idk
* **sculpt**: Maya-like sculpting for simple, (destruktive) changes

### L-Systems:
WIP

Recreating the L-Systems SOP using vex and python to allow additional functions and making the overall workflow easier and more art-directable.

This includes the LEO_L-System SOP and some vex functions. Those functions are found inside the vex folder.
