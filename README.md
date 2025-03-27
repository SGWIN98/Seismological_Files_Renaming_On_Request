# **Batch File Renamer for Timestamped Files**  

## **Overview**  
This Python script renames files with a specific timestamp pattern by **reducing the first timestamp’s minutes by 10** and **removing the second timestamp**, while preserving the file’s prefix and suffix.  

### **Example Before & After:**  
| **Before** | **After** |
|------------|----------|
| `Y2_NPUK_200707150938_200707150948_HHE` | `Y2_NPUK_200707150928_HHE` |
| `Y2_NPUK_200707150938_200707150948_HHN` | `Y2_NPUK_200707150928_HHN` |
| `Y2_NPUK_200707150938_200707150948_HHZ` | `Y2_NPUK_200707150928_HHZ` |

✅ **Test files** are included in the repository to verify the script’s functionality.

---

## **Features**  
✔ **Automatic detection** of timestamped filenames  
✔ **Reduces the first timestamp’s minutes by 10**  
✔ **Removes the second timestamp** entirely  
✔ **Works for any prefix and suffix**  
✔ **Batch renaming support**  

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
Open `rename_files.py` and modify the `folder_path` variable to match your target directory.

### **4️⃣ Run the Script**  
```sh
python rename_files.py
```

---

## **Test Files**  
The repository includes sample test files like:  
```
Y2_NPUK_200707150938_200707150948_HHE
Y2_NPUK_200707150938_200707150948_HHN
Y2_NPUK_200707150938_200707150948_HHZ
```
After running the script, they will be renamed as follows:  
```
Y2_NPUK_200707150928_HHE
Y2_NPUK_200707150928_HHN
Y2_NPUK_200707150928_HHZ
```
You can add more test files following the same pattern to verify the script.

---

## **License**  
This project is open-source under the **MIT License**.  

---

### **Contributions**  
Feel free to **fork the repository**, improve the script, and submit a **pull request**! 🚀  
