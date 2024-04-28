import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error
import tkinter as tk
from tkinter import ttk  


df = pd.read_csv("Fertilizer Recommendation.csv")
le = LabelEncoder()
df["Crop Type"] = le.fit_transform(df["Crop Type"])
df["Soil Type"] = le.fit_transform(df["Soil Type"])
df["Fertilizer Name"] = le.fit_transform(df["Fertilizer Name"])
x = df.drop(columns=['Fertilizer Name'])
y = df["Fertilizer Name"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

rf = RandomForestClassifier()
rf.fit(x_train, y_train)
dc = DecisionTreeClassifier()
dc.fit(x_train, y_train)
s = SVC()
s.fit(x_train, y_train)
kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(x_train, y_train)
root = tk.Tk()
root.title("Fertilizer Recommendation")

label = tk.Label(root, text="Select Crop Type:")
label.grid(row=0, column=0)

combo = ttk.Combobox(root, values=df["Crop Type"].unique())
combo.grid(row=0, column=1)
def get_recommendation():
    crop_type = combo.get()  
    encoded_crop_type = le.transform([crop_type])[0]
    
    
    input_data = pd.DataFrame({
        "Temperature": [26],  
        "Humidity": [52],
        "Moisture": [38],
        "Soil Type": [1],  
        "Crop Type": [encoded_crop_type],
        "Nitrogen": [0],
        "Potassium": [0],
        "Phosphorous": [0]
    })
    
   
    pred_rf = rf.predict(input_data)
    pred_dc = dc.predict(input_data)
    pred_s = s.predict(input_data)
    pred_kn = kn.predict(input_data)
    
    
    pred_rf_fertilizer = le.inverse_transform([pred_rf])[0]
    pred_dc_fertilizer = le.inverse_transform([pred_dc])[0]
    pred_s_fertilizer = le.inverse_transform([pred_s])[0]
    pred_kn_fertilizer = le.inverse_transform([pred_kn])[0]
    
    
    result_label.config(text=f"Random Forest: {pred_rf_fertilizer}\n"
                              f"Decision Tree: {pred_dc_fertilizer}\n"
                              f"SVM: {pred_s_fertilizer}\n"
                              f"KNN: {pred_kn_fertilizer}")


button = tk.Button(root, text="Get Recommendation", command= get_recommendation)
button.grid(row=1, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=2)

def get_recommendation():
    crop_type = combo.get()


root.mainloop()

