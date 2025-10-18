# BIM Analyst Group 13 
## Assignment 2 

### A2a) Python knowledge
**How much do you agree with the following statement:**
*I am confident in coding with python*

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













