import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'D:\project\Employee_Attrition\employee_200.csv')


print("Dataset Head:\n", data.head())
print("\nMissing Values:\n", data.isnull().sum())
data['Attrition'] = data['Attrition'].fillna('No')  
data = data.dropna() 

# Attrition Count Plot
attrition_counts = data['Attrition'].value_counts()
plt.figure(figsize=(5,5))
attrition_counts.plot(kind='pie', autopct='%1.1f%%', colors=['#66b3ff','#ff9999'])
plt.title('Employee Attrition Distribution')
plt.ylabel('')
plt.show()

# Department-wise Attrition
dept_attrition = data[data['Attrition'] == 'Yes']['Department'].value_counts()
plt.figure(figsize=(8,4))
dept_attrition.plot(kind='bar', color='#ff6666')
plt.title('Attrition Count by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45) 
plt.show()

# Age Distribution of Employees
plt.figure(figsize=(8,4))
plt.hist(data['Age'], bins=10, color='#66b3ff', edgecolor='black')
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Years at Company vs Attrition
plt.figure(figsize=(8,5))
data[data['Attrition'] == 'Yes']['YearsAtCompany'].hist(alpha=0.7, label='Attrition = Yes', color='red')
data[data['Attrition'] == 'No']['YearsAtCompany'].hist(alpha=0.7, label='Attrition = No', color='blue')
plt.title('Years at Company vs Attrition')
plt.xlabel('Years at Company')
plt.ylabel('Number of Employees')
plt.legend()
plt.show()
print("\n--- Analysis Completed ---")
