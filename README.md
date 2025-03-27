# **Batch File Renamer for Timestamped Files**  

## **Overview**  
This Python script renames files with a specific timestamp pattern by **reducing the first timestamp’s minutes by 10** and **removing the second timestamp** while preserving the file’s prefix and suffix.  

### **Example Before & After:**  
| **Before** | **After** |
|------------|----------|
| `Y2_NPUK_200707150938_200707150948_HHE` | `Y2_NPUK_200707150928_HHE` |
| `X1_TEST_201905221015_201905221025_ABC` | `X1_TEST_201905221005_ABC` |

## **Features**  
✅ Automatically detects files with timestamped names  
✅ Reduces the **first timestamp’s minute value by 10**  
✅ Removes the **second timestamp** entirely  
✅ Works for **any prefix** and **any suffix**  
✅ Supports **batch renaming** in a specified folder  

---

## **Usage**  
### **1️⃣ Install Python (if not installed)**  
Ensure Python 3.x is installed on your system.  

### **2️⃣ Clone the Repository**  
```sh
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

### **3️⃣ Edit the Folder Path**  
Open `rename_files.py` and modify the `folder_path` variable to point to the directory containing your files.

### **4️⃣ Run the Script**  
```sh
python rename_files.py
```

---

## **How It Works**  
- The script uses **regular expressions** to detect filenames that match the format:  
  ```
  {prefix}_{YYYYMMDDHHMM}_{YYYYMMDDHHMM}_{suffix}
  ```
- It **extracts the first timestamp**, decreases the **minutes by 10**, and constructs a **new filename**.
- The **second timestamp is removed**, and the file is renamed accordingly.

---

## **Example Folder Structure**  
```
📂 Your Folder  
 ├── Y2_NPUK_200707150938_200707150948_HHE  ➝  Y2_NPUK_200707150928_HHE  
 ├── Y2_NPUK_200707150938_200707150948_HHN  ➝  Y2_NPUK_200707150928_HHN  
 ├── Y2_NPUK_200707150938_200707150948_HHZ  ➝  Y2_NPUK_200707150928_HHZ  
```

---

## **License**  
This project is open-source under the **MIT License**.  

---

### **Contributions**  
Feel free to **fork the repository**, improve the script, and submit a **pull request**! 🚀 
