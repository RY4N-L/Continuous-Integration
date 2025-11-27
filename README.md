# DAT5501 Continuous Integration & Data Pipeline

This repository contains activities for the DAT5501 module focused on **Continuous Integration (CI)** with CircleCI and the development of a **data validation pipeline**.  
Each folder demonstrates professional repository curation, automated testing, and iterative development practices.

---

## 🌟 Highlights

- Configured **CircleCI** for automated testing linked to GitHub.  
- Implemented **unit testing frameworks** with both `unittest` and `pytest`.  
- Built a **synthetic data pipeline** for line fitting and validation.  
- Automated checks for data integrity (numeric values, saved files, tolerance checks).  
- Generated plots comparing **original input line vs best-fit line**.  
- Demonstrated iterative commits with passing/failing builds to validate CI workflow.  

---

## 📂 Folder Structure

- **.circleci ⚙️**  
  - `config.yml` – CircleCI configuration file (Python 3.8 Docker image, installs dependencies, runs tests).  

- **Continuous-Integration-activity 🔄**  
  - `test_function.py` – simple function to add two numbers.  
  - `test_suite.py` – unit tests using `unittest`.  
  - `test_suite_alternative.py` – unit tests using `pytest` assertions.  

- **Data-Pipeline-CI-activity 📊**  
  - `generate_and_plot_random_linear_data.py` – generates noisy linear data, saves to CSV, and plots best-fit line vs original line.  
  - `plot_random_linear.py` – loads CSV and plots best-fit line.  
  - `random_linear_data.csv` – generated dataset of X and Y values.  
  - `random_linear_plot.png` – saved plot of data and fitted line.  
  - `static_linear_data.csv` – static dataset for validation.  
  - `test_suite_linear_fit.py` – unit tests for data pipeline (numeric checks, file creation, slope/intercept tolerance).  
  - `test_random_linear_data.csv` – test dataset.  
  - `test_random_linear_plot.png` – test plot.  

- **requirements.txt 📦**  
  - Contains dependencies: `pytest`, `numpy`, `pandas`, `matplotlib`.  

---

## ⚙️ Requirements

- Python 3.8+  
- Install dependencies:
```bash
pip install -r requirements.txt
```

🚀 How to Run
Clone the repository:

```bash
git clone https://github.com/RY4N-L/Continuous-Integration.git
cd CI_pipeline
```

Run the Continuous Integration activity:

```bash
cd Continuous-Integration-activity
pytest test_suite_alternative.py
```

Run the Data Pipeline activity:

```bash
cd Data-Pipeline-CI-activity
python generate_and_plot_random_linear_data.py
pytest test_suite_linear_fit.py
```

---
## 📝 Outstanding Tasks / To‑Do

- [ ] Add error bars to synthetic data and update fitting routine.
- [ ] Handle missing/NaN values gracefully in pipeline.
- [ ] Extend models to quadratic/exponential fits.
- [ ] Add goodness-of-fit metrics (χ², R²).
- [ ] Explore maximum-likelihood fitting with [emcee](https://emcee.readthedocs.io/en/stable/tutorials/line/).

---
