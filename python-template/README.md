# Using the Python Template

To use the python template by default in newly created dynamo python nodes, add the following line (with indent) to the DynamoSettings.xml file located in
`%Appdata%\Dynamo\Dynamo Revit\[version number]`, changing as necessary to point to your python template file path and replacing the existing `<PythonTemplateFilePath />` line.

```
  <PythonTemplateFilePath>%appdata%\Dynamo\Dynamo Revit\<dynamo version>\DynamoPythonTemplate.py</PythonTemplateFilePath>
```
