# LEO_Tools:
A collection of HDAs for SideFX Houdini.
I'll upload them whenever I created a new one for my projects.

Also I'll add some usefull code to the useful folder whenever I encounter something cool.

They are made with Houdini **Indie** and only work with Indie, Apprentice or Educational.

## List of current HDAs:
### SOP:
* variantMerge: Merges Geometry and adds a variant attribute to be used with the H18 "copy to points"-SOP.
* alignPoint: Align Geometry to another Geometry based on a selected Point (currently only one point for Source and Target supported) 

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
The houdini.env on Windows 10 should be located at c:\users\[username]\Documents\houdini[version]

Add following to the env but change the "LEO" path to the downloaded directionary

```
LEO="E:/Projects/LEO_Tools"

HOUDINI_PATH=$LEO;$HOUDINI_PATH;&
```


