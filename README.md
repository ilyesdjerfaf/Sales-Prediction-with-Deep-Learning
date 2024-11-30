# 📊 Sales Prediction with Deep Learning 🤖

Welcome to the **Sales Prediction with Deep Learning** repository! This project takes you through an exciting journey of exploring and analyzing time-series sales data, performing stationarity studies, and implementing machine learning and deep learning models to predict sales with high accuracy.

---

## 🔄 Project Workflow

### 1. 🕵️ Data Exploration
I started by exploring the data to understand its structure, patterns, and key insights. This stage allowed me to identify trends and seasonality in the sales data.

### 2. 📈 Time Series Analysis
I performed a detailed time series analysis to study the stationarity of the data using various techniques:
- **Log Transformation**: Reduces variance across data points.  
  Formula: $y = \log(x)$
- **Differencing**: Removes trends to achieve stationarity.  
  Formula: 
  $y_t' = y_t - y_{t-1}$
- **Box-Cox Transformation**: Stabilizes variance and normalizes the distribution.  
  Formula: 
  $y(\lambda) = \frac{x^\lambda - 1}{\lambda}, \; \text{if } \lambda \neq 0$
- **Fourier Transformation**: Decomposes data into frequency components for seasonality analysis.  
  Formula: 
  $f(x) = a_0 + \sum_{n=1}^{N} \big[ a_n \cos(nx) + b_n \sin(nx) \big]$

These techniques helped preprocess the data and prepare it for effective modeling.

### 3. 🧠 Model Development
I experimented with various machine learning and deep learning models using an **MLOps approach**. With **MLflow**, I monitored and tracked the performance of all models, ensuring transparency and reproducibility. The best-performing model has been saved as a `.pkl` file for easy deployment in applications.

---

## 🚀 Future Work
I aim to:
- Develop a user-friendly interface to allow users to interact with the model and explore its potential for sales forecasting.
- Enhance the model’s capabilities for real-time sales predictions.

---

## 🛠️ Technologies

### 🔹 **Python**  
<div style="width: 100px;">
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" alt="Python">
</div>
The core programming language used to develop the project.

### 🔹 **Scikit-Learn**  
<div style="width: 100px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-Learn">
</div> 
Used for implementing machine learning models and preprocessing.

### 🔹 **Statsmodels**  
<div style="width: 100px;">
    <img src="src/statsmodels.png" alt="Statsmodels">
</div>
A library for statistical analysis and time series modeling.

### 🔹 **MLflow**  
<div style="width: 100px;">
    <img src="src/mlflow.png" alt="MLflow">
</div>
An open-source platform for tracking experiments, packaging code, and sharing models. 
An open-source platform for tracking experiments, packaging code, and sharing models.

### 🔹 **Pickle**  
Used to save and load the best model for deployment.

### 🔹 **GitHub Actions**  
<div style="width: 100px;">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Actions">
</div> 
Automated workflows for CI/CD pipelines.

---

## 🛠️ Getting Started

Follow these steps to run the project:

1. **Clone the repository**:

```bash
   git clone https://github.com/ilyesdjerfaf/Sales-Prediction-with-Deep-Learning.git
   cd Sales-Prediction-with-Deep-Learning
```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   ```

4. **Run MLflow**:
   Start the MLflow UI to track the experiments:
   ```bash
   mlflow ui
   ```
   Access it at: [http://localhost:5000/](http://localhost:5000/)  
   Ensure that port **5000** is free before running the above command.

---

## 🤝 Collaboration and Contributions

I welcome contributions! Please refer to the [CONTRIBUTING.md](./CONTRIBUTING.md) file for guidelines on how to collaborate on this project.

---

## 📧 Contact

For any queries or collaboration opportunities, feel free to reach out through the repository.

---