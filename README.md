# Customer Segmentation using K-Means Clustering

This project uses K-means clustering to segment customers of a mall based on three features: Age, Annual Income, and Spending Score. The goal is to group customers into clusters that exhibit similar behaviors, which can be helpful for targeted marketing or analysis.

## Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Data](#data)
- [Steps](#steps)
- [How to Run](#how-to-run)
  - [On Windows](#on-windows)
  - [On macOS/Linux](#on-macoslinux)
- [License](#license)

## Introduction

The project applies machine learning (specifically, K-means clustering) to segment customers based on their demographic and behavioral data. The dataset includes the following key features:
- **Age**: Age of the customer
- **Annual Income (k$)**: Annual income of the customer in thousands of dollars
- **Spending Score (1-100)**: Spending score assigned to the customer, where 1 indicates low spending and 100 indicates high spending.

By applying K-means clustering, we divide customers into 5 distinct clusters. This can help businesses understand customer groups better and tailor marketing strategies accordingly.

## Dependencies

The following Python libraries are required to run the project:
- `pandas` – For data manipulation and handling CSV files
- `sklearn` – For machine learning algorithms and preprocessing
- `matplotlib` – For data visualization

To install the required dependencies, use:
```bash
pip install pandas scikit-learn matplotlib
```

## Data

The data used for this project is stored in a CSV file located at `Data_set/Mall_Customers.csv`. The dataset contains information about various customers, with columns for Age, Annual Income, Spending Score, and additional demographic information (e.g., gender).

Example of the dataset format:

| CustomerID | Gender | Age | Annual Income (k$) | Spending Score (1-100) |
|------------|--------|-----|---------------------|------------------------|
| 1          | Male   | 19  | 15                  | 39                     |
| 2          | Male   | 21  | 15                  | 81                     |
| 3          | Female | 20  | 16                  | 6                      |

## Steps

The process consists of the following steps:

1. **Loading the Dataset**: 
   - Read the CSV file into a Pandas DataFrame.

2. **Selecting Features**: 
   - Select relevant features for clustering: `Age`, `Annual Income (k$)`, and `Spending Score (1-100)`.

3. **Feature Scaling**: 
   - Standardize the features using `StandardScaler` from scikit-learn to ensure all features have the same scale, which improves the K-means clustering results.

4. **K-Means Clustering**: 
   - Apply the K-means clustering algorithm with 5 clusters. The number of clusters is chosen based on the assumption that the customer base can be segmented into five distinct groups.

5. **Adding Cluster Labels**: 
   - Append the cluster labels to the original dataset for easy reference.

6. **Centroids**: 
   - Get the centroids of each cluster and transform them back to the original scale for visualization.

## How to Run

To run the project, follow these steps:

### On Windows

1. **Install Dependencies**:
   - Open Command Prompt or PowerShell.
   - Navigate to your project directory using the `cd` command. For example:
     ```bash
     cd C:\path\to\your\project
     ```
   - Install the necessary Python libraries:
     ```bash
     pip install pandas scikit-learn matplotlib
     ```

2. **Run the Script**:
   - In the same Command Prompt or PowerShell window, run the Python script:
     ```bash
     python your_script_name.py
     ```

### On macOS/Linux

1. **Install Dependencies**:
   - Open Terminal.
   - Navigate to your project directory using the `cd` command:
     ```bash
     cd /path/to/your/project
     ```
   - Install the necessary Python libraries:
     ```bash
     pip install pandas scikit-learn matplotlib
     ```

2. **Run the Script**:
   - In the same Terminal window, run the Python script:
     ```bash
     python your_script_name.py
     ```

Replace `your_script_name.py` with the actual name of the Python script you are running.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
