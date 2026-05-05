# Website-Phishing-Detection

## Introduction

This project is for my final year dissertation. It consists of two primary parts:

- Notebook research on finding the best model among three different tree classifier algorithms (Decision Tree, Random Forest, and Gradient Boosting) using balanced and imbalanced data. The original dataset can be found at: https://data.mendeley.com/datasets/c2gw7fy2j4/3

- Dashboard on research results and a URL phishing detector tool.

Once all dependencies are installed and the Jupyter Lab notebooks are run, the entire project is approximately 1.5 GB large.

Please read through all sections to understand how to run both the research notebooks and dashboard.

## Directory Structure Explained

- Web_Phish_Project is the root directory.

- dashboard contains all Streamlit dashboard logic, including pages, route definitions, and a configuration file. Additionally, a requirements.txt 
  file contains all the necessary python libraries required to run the dashboard application.

- feature_extraction contains the logic necessary to extract all the required features from a URL.

- research_notebooks contains two notebooks which explore the chosen dataset, classifier model parameter tuning, model training, model testing,
  SHAP explanations, and image and data generation, saving, and loading. Moreover, requirements.txt file contains all the necessary python libraries
  required to run the notebooks.

- saved_data contains the images and data results. Trained models and a URL dataset can be generated from running the notebooks. 

## ⚠️ Requirements

- Python must be installed on your local machine.
  
- Download the detector tool from https://github.com/AntDBuck/Website-Phish-Detection/releases/tag/v1.0 and store the file in the saved_data/trained_models/ directory.

Note: You can also generate the detector model from the running of the notebooks but this can take approximately 1 to 2 hours.

## Installation Instructions

Note: Choose either the automatic or manual installation process, not both.

### Automatic Setups

1. Open CMD/terminal.

2. Move prompt to either research_notebooks or dashboard.

3. Run setup script:
  ```
  python setup.py
  ```

### Manual Setups

Repeat this process twice, once for notebooks and the other for dashboard.

1. Open CMD/terminal.

2. Move prompt to either research_notebooks or dashboard directory.

3. Create a python virtual environment to hold dependencies:
  ```
  python -m venv .venv
  ```

4. Activate virtual environment:

   (Windows) >
   ```
   .venv\Scripts\activate
   ```

   (MacOS/Linux) >
   ```
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
   
## Startup Instructions

1. Open CMD/terminal.

2. Move prompt to either research_notebooks or dashboard directory.

3. Activate virtual environment:

   (Windows) >
   ```
   .venv\Scripts\activate
   ```
   
   (MacOS/Linux) >
   ```
   source .venv/bin/activate
   ```

4. If in research_notebooks directory, Run Jupyter Lab:
   ```
   jupyter lab
   ```
   
   If in dashboard directory, Run Streamlit app:
   ```
   streamlit run app.py
   ```

# Thank You For Reading!
