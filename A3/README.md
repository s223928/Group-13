# About the tool

State the problem / claim that your tool is solving.
State where you found that problem.


# Description of the Tool

This tool is designed to **analyze building models** and provide **ventilation estimates for each room**. By inputting the building’s **MEP and ARCH files**, along with its **EIQ category** and **pollution level**, the tool calculates the **floor area, occupancy, and estimated ventilation rates** for every room.  
The output is saved as a **CSV file**, making it easy to review, share, or integrate into further analyses. 


# Instructions to Run the Tool

1. **Download the required scriots and modules in the file FINAL** before running the tool.

2. **Initiate the main script.** From this point onward, all interaction will take place in the terminal.

3. You will first be asked to **enter the file paths** for two model files: **MEP** and **ARCH**.  
   - Type in the full paths and press **Enter**.

4. Next, you will be asked to **enter the EIQ category**.  
   - The most common category is **2**, but enter the value that corresponds to your building.

5. You will then be asked to **enter the building’s pollution level**, which you should know or can find in DS.

6. The tool will **create a CSV file** in the same folder as the scripts, FINAL.  
   - Open this file to see:  
     - All rooms in the building  
     - Their usage  
     - Floor area  
     - Approximated occupancy  
     - Estimated ventilation rates required for each room

7. To run a different model, simply **clear the terminal** and run the script again.


# Advanced Building Design

## Advanced Building Design Stage
The tool is most useful during **Stage C or D**:  
- **Stage C** – Detailed Design: The model is developed enough to include room layouts, MEP systems, and basic building parameters, allowing accurate ventilation estimations.  
- **Stage D** – Construction Documentation: Fully coordinated models can be validated for ventilation, occupancy, and floor area compliance before final construction documents are issued.  

## Subjects That Might Use It
The tool could be valuable for:  
- **Building Engineering** – analyzing ventilation needs and occupancy calculations  
- **Architecture** – reviewing models level of completion and usefulness 
- **HVAC/MEP Engineering** – validating mechanical systems and air distribution  

## Required Model Information
For the tool to function correctly, the model must include:  
- **MEP files** – mechanical, electrical, and plumbing systems  
- **ARCH files** – architectural layouts including rooms and floor plans  
- **Room usage/type** – what each room is for (office, classroom, lab, etc.)  
- **Floor area** – size of each room  
- **Air quility** - Pollution level or EIQ category to refine ventilation estimates
- **Optional:** Occupancy information
