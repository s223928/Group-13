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
