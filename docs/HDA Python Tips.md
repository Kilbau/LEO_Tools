# Action Button Group #
### Use this code inside the "Action Button" Tab for **String Parameters**:

```python
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

### For a group dropdown menu 
enable **Use Menu** under Menu and change the dropdown to **Toggle (Field + Multiple Selection Menu)**

### To get the little arrow symbol

add a new Tag on the Parameter Menu

Tag Name: script_action_icon

Tag Value: BUTTONS_reselect

# Callback Script #
It is possible to call a function from a parameter. For example when a button is pressed or a value changed.

The easiest way is defining the functions in  "scripts" - "PythonModule".
Then in the parameter callback script field run the script.
``` python
hou.phm().myFunction(kwargs) #replace myFunction
```

# Scripts Tab define functions #
When multiple events (e.g. OnCreated, OnDeleted ...) are supposed to call the same function, it is easiest to define it in another file.

First create the extra file using the "Event Handler" dropdown using "Custom Script".
Then define the function as normal.
To call the function use this code.
```python
import toolutils

mymodule = toolutils.createModuleFromSection("mymodule", kwargs['type'], "myCustomScript") #replace myCustomScript
mymodule.myFunction(kwargs) #replace myFunction() 
```

# On Copy Event #
There sadly currently is no event to call code when a node is copied. To work around this user Stalkerx777 on odforce created following script to check if the node is beeing copied.

```python
def is_copy_paste_event(kwargs):
    #code by Stalkerx777 on odforce
    if not kwargs['node'].name().startswith('original') and not kwargs['old_name'].startswith('original'):
        original_node = kwargs['node'].parent().node('original0_of_%s' % kwargs['old_name'])
        return True if original_node else False
```

# Unordered Inputs #
Nodes like the merge node have so called "unordered inputs". This means that the order of the connections doesn't matter.

When a HDA has 28 or more inputs the inputs are displayed as a long solid bar (like the merge sop) but unlike the merge sop those inputs are still ordered. This can cause some problems.

For example the "Variant Merge" allows up to 9999 inputs. If the user has 5 inputs connected but decides to remove input number 3. The HDA will still loop over the 5 inputs. This might cause issues when using the current loop iteration as an attribute because the geos will now have values like 0,1,3,4.

To fix this the Variant Merge sop has an "OnInputChanged" event. This event removes all current connections and rewires them in the same order but skipping empty connections.
This code requires a "cleanstate" integer parameter because every connection that is modified by the script would also call the "OnInputChanged" event which would cause infinte loops and finally crashes Houdini.

```python
def orderInputs():
    """ 
    problem with ordered inputs:
    if inputs are removed they leave empty connections
    this causes problems with the numvar attribute because the empty connections are still counted
    
    deletes all inputs and reconnnects them to remove empty connections
    """
    node = kwargs["node"]
    
    # sets parameter on the hda to avoid triggering the OnInputChanged event every time this function changes the inputs
    stateparm = node.parm("cleanstate")
    stateparm.set(1)
    
    # save current connections
    connections = node.inputConnections()
    
    # remove all connections 
    for idx in range(len(node.inputs())):
        node.setInput(idx,None,0)
    
    # rewire input connections to remove empty connections
    for idx, input_con in enumerate(connections):
        
        input_node = input_con.inputNode()
        output_idx = input_con.outputIndex()
        
        node.setInput(idx, input_node, output_idx)
    
    stateparm.set(0)
        
    
if not kwargs["node"].parm("cleanstate").eval():
    orderInputs()
```

