import pandas as pd
import numpy as np
# Create sample student data
np.random.seed(42)
# Generate sample data
departments = ['Computer Science', 'Information Technology', 'AI & DS', 'Cyber Security']

data = {
    'roll_number': np.arange(1, 366),
    'department': np.random.choice(departments, 365),
    'attendance': np.random.uniform(65, 100, 365),
    'marks': np.random.normal(75, 20, 365),
    
}
# Ensure marks are between 0 and 100
data['marks'] = np.clip(data['marks'], 80, 100)

df = pd.DataFrame(data)

print(df)
print("Sample of the Vels University student dataset:")
print(df.head())
df.to_excel("vels_university_students.xlsx", index=False)
u1=23625121
pass1=1234
user=int(input("Enter your roll number: "))
password=int(input("Enter your password: "))
print("1. View Attendance\n2. View Marks\n3. View Department")
choice=int(input("Enter your choice:"))
if(user==u1 and password==pass1):
    print("Login Successful")
    if(choice==1):
            print("Your attendance is:", df.loc[df['roll_number']==user, 'attendance'].values[0])
            
    if(choice==2):
            print("Your marks are:", df.loc[df['roll_number'] == user, 'marks'].values[0])
            
    if(choice==3):    
            print("Your department is:", df.loc[df['roll_number'] == user, 'department'].values[0])
    else:
            print("Invalid choice")


