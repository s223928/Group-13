# BIM Analyst Group 13 
## Assignment 2 

### A2a) Python knowledge
**How much do you agree with the following statement:**
*I am confident in coding with Python*

Score: 1 - Disagree 
(We are still developing our Python skills but are learning and improving through this project).

#### Group focus area:
Our group’s focus area is building performance analysis, specifically in relation to indoor environmental quality (IEQ) and ventilation performance.
We are taking an analyst role, focusing on data extraction, verification, and calculation,

### A2b) Identifying a claim 
#### Selected Building:
Building 2508 (ARCH and MEP models)

#### Claim / Issue to Check:
We aim to verify whether the ventilation design for Building #2508 complies with the requirements specified in DS/EN 16798-1:2019 regarding the minimum outdoor air supply rates for different room types and occupancy categories.

#### Description of the claim:
The project report assumes that all rooms in Building #2508 meet the minimum required ventilation rates defined by the standard. We plan to test this assumption by developing a Python-based BIM data extraction and validation tool that retrieves room geometry, occupancy, and ventilation system data directly from the ARCH and MEP models, and then performs calculations to compare actual ventilation rates against required values.

#### Justification for selecting this claim:
We chose this claim because:
- Ventilation directly affects indoor air quality and occupant comfort, which are central to sustainable building design.
- The verification process requires integrating information from multiple BIM models (ARCH + MEP), which provides a meaningful challenge and learning opportunity.
- The task helps us develop practical Python skills in BIM data handling, parametric analysis, and compliance checking.

### A2c) Use Case
#### The tool will: 

1. Extract data from the ARCH and MEP BIM models using Python.
2. Link and match the extracted data between ARCH and MEP models
3. Calculate the required ventilation rate per room according to DS/EN 16798-1:2019 based on occupancy and activity levels.
4. Compare the calculated requirement with the design airflow values extracted from the MEP model.
5. Assess whether the ventilation provided is sufficient for code compliance.

#### When would this claim need to be checked?
During the design phase, before the construction phase begins — ideally as part of design validation or quality control to ensure compliance with ventilation standards.

#### Information this claim relies on:

- Room geometry and area (from ARCH model)
- Occupancy or room type (from ARCH model)
- Total Airflow supply rate (from MEP model)
- Standard ventilation rate requirements (from DS/EN 16798-1:2019)

#### BIM purpose:
Analyse (with some aspects of Generate and Communicate): The tool analyses BIM model data to verify compliance with environmental performance standards.


### A2e) Tool idea 
#### **Description:**
**Ventilation Check** will be a Python-based OpenBIM tool that automatically performs ventilation compliance checks using IFC models.
It uses ifcOpenShell to read the ARCH and MEP models, extract room and ventilation data, and then compare design values against the requirements. The outcomes are:
- Minimum DS/EN 16798-1:2019 thresholds for our building
- Required air flow
- Compliance status (Pass / Fail), when data is available
- Deviation (%)

#### **Business and Societal Value:**
This tool will streamline the process of informing MEP designers about the required ventilation rate thresholds for each room in accordance with local regulations and standards such as DS/EN 16798-1:2019. It automates the entire compliance check by using the BIM model itself as the primary source of information for calculating and verifying the required airflow rates. Because it is based on open standards and developed in Python, the tool can be easily adapted and reused for future projects, promoting knowledge sharing, interoperability, and continuous improvement within the OpenBIM community.

### A2f) Information requirementRoom area
#### **Room area:**
- Source: ARCH model
- IFC: IfcSpace (area or geometry)
- In model:  Yes
- Retrieval with ifcOpenShell: Yes 

#### **Room height:**
- Source: ARCH model
- IFC: IfcSpace (height)
- In model: Yes
- Retrieval with ifcOpenShell: Yes 

#### **Room use:**

- Source: ARCH model 
- IFC: IfcSpace 
- In model: Yes
- Retrieval with ifcOpenShell: Yes 

#### **Provided airflow:**

- Source: MEP model
- IFC: IfcUnitaryEquipment, IfcDuctSegment, IfcAirTerminal
- In model: Yes 
- Retrieval with ifcOpenShell: Yes (provided correct and sufficient data is available)

#### **Reference ventilation rates:**

- Source: external file (DS/EN 16798-1:2019 based on occupancy and activity levels)
- IFC: no
- In model: no
- Retrieval with ifcOpenShell: no (load from external data)

#### **What we need to learn:**

- How to read IfcSpace and property sets with ifcOpenShell
- How to extract and collect relevant data to input in the formulas for calculations.
- How to load external data and apply them to calculations

### A2g) Software licence

We have chosen to release our project under the **MIT License**. This licence is simple and widely used, allowing others to freely use, modify, and distribute our code with minimal restrictions. By doing so, we encourage collaboration and reuse, enabling other students, researchers, and professionals to build upon our work.












