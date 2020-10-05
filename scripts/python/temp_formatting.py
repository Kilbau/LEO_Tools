dict0 = {  # Title || section Headers
    "value": "Title",
    "syntax": "== {value} ==",
}

dict1 = {  # Type
    "name": "icon",
    "value": "opdef:.?Icon.svg",
    "syntax": "#{name}: {value}",
}

dict2 = {  # Type
    "name": "type",
    "value": "node",
    "syntax": "#{name}: {value}",
}

dict3 = {  # Summary
    "value": "Summary in one or two sentences.",
    "syntax": '""" {value} """',
}

dict4 = {  # Sections
    "value": "inputs",
    "syntax": "@{name}",
}

dict5 = {  # Parameter
    "label": "External Label",
    "name": "internal_name",
    "value": "Description of paramter.",
    "syntax": "{}:\n\t#id: {}\n\n\t{value}",
}

list_ = [dict1, dict2, dict3]
# print(dict5["syntax"])


# Todo:
# create a class inside the other class for those functions
# init with name, label, value, syntaxname
# the syntaxname looks up a dict to get the correct syntax for the type
syntax_dict = {
    "parameter": "{label}\n\t#id: {name}\n\n\t{value}",
    "section": "@{name}",
    "info": "#{name}: {value}",
    "header": "== {name} ==",
    "summary": '""" {value} """',
    "video": ":video:\n\t#src:{value}",
    "reference": "[{name}:{value}]",  # name: Image/Node/Include
}


class Template:
    def __init__(self, syntax_dict, name="", label="", value="", category=""):
        pass

    # create and set the ui.
