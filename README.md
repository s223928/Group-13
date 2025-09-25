# BIManalyst group 13 

### Focus Area 

#### Indoor Environment 

### Claim 
The claim we are checking for the first assignment is the ammount of storeys within the building model no. 16. Through our "discovery" phase of the ifcopenshell library we decided to examine whole building claims within the report. Specifically for this assignment we will be checking the ammount of storeys within the building. Our scope is to cross-check whether the data within the ifc Architecture model corresponds to the project report. 

### Supporting Evidence 
The floor plans and building levels supporting this claim are presented in the **Architectural Project Report, pages 5–7.**

### Method

We used a Python script with the IfcOpenShell library to:

1. Open the IFC Architectural model.
2. Retrieve all entities of type IfcBuildingStorey.
3. Extract the storey names and elevations.
4. Count floors above ground (elevation ≥ 0) and below ground (elevation < 0).
5. Compare the result against the report’s claim of 5 floors above ground and 1 underground.

### Script Used

```python
import ifcopenshell

model = ifcopenshell.open('25-16-D-ARCH.ifc')

storeys = model.by_type('IfcBuildingStorey') # Find all storeys

print('=== Storeys found in the model ===') 
above = 0
below = 0
for s in storeys: 
    name = s.Name  
    elevation = getattr(s, 'Elevation', None)  # Extract elevation attribute if it exists
    print(f'Storey: {name}, Elevation: {elevation}')

    # Count floors above/below ground
    if elevation is not None:
        if elevation >= 0:
            above += 1
        else:
            below += 1

print('Summary:')
print(f'Floors above ground: {above}')
print(f'Floors underground: {below}')

# Validation of claim
if above == 5 and below == 1:
    print('Claim validated: 5 floors above ground and 1 underground')
else:
    print('Claim not validated')
```

### Interpeting Results

Our script indicates **two underground** in the IFC model, whereas the report describes one. A likely explanation, especially for a Revit-authored model, is that two closed spaced Levels (i.e. top of slab and bottom slab, ~300 mm apart) were both exported as IfcBuildingStorey. This is a common setup for coordination and does not imply an incorrect design; it may simply reflect how levels were defined and mapped during export. The reason we picked this claim is because this distintion of storeys could matter for downstream work. Analyses that groupd data by storey, such as areas and volumes which are asssociated indoor environment analysis, could include the extra level and slightly skew the results. 