Use this code inside the "Action Button" Tab for **String Parameters**:

```
import soputils
kwargs['geometrytype'] = hou.geometryType.Points
kwargs['inputindex'] = 0
soputils.selectGroupParm(kwargs)
```
 
change the Points to the required selection type:
* Edges
* Points
* Primitives
* Vertices

change the 0 to the current nodes input

For a group dropdown menu 
enable **Use Menu** under Menu and change the dropdown to **Toggle (Field + Multiple Selection Menu)**

To get the little arrow symbol

add a new Tag on the Parameter Menu

Tag Name: script_action_icon

Tag Value: BUTTONS_reselect
