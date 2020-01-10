Use this code inside the "Action Button" Tab:

```import soputils
kwargs['geometrytype'] = hou.geometryType.Points
kwargs['inputindex'] = 0
soputils.selectGroupParm(kwargs)```