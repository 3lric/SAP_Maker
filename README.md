# SAP Maker

**Version:** 0.2b  
**Author:** 3lric  
**License:** MIT License  

### **Overview**
SAP Maker is a tool designed to assist in extracting and creating SAP (Sound Archive Package) files, commonly used in video games. The application allows users to extract WAV audio files from SAP files and create new SAP files using WAV files. 

### **Features**
- Extract multiple WAV files from an SAP archive.
- Rebuild SAP files from a set of WAV files.
- Support for different types of SAP files, including:
  - Core
  - Door
  - Enemy
  - Room
  - Weapon
  - Voice/Music
  - Footstep
  - Custom
- User-friendly interface for easy SAP manipulation.
- Displays warnings when working with "Custom" SAP types, which require special handling.

**Currently, SAP Maker only works with Resident Evil 2 / Biohazard 2 SAP files.**

### **System Requirements**
- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `Pillow`
  - `os`
  - `webbrowser`

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/3lric/SAP_Maker.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Build the executable using PyInstaller (optional):
   ```bash
   pyinstaller --onefile --windowed --icon=SM_Icon.ico --add-data "SM_Icon.ico;." --add-data "logo.png;." --add-data "sap_files.py;." --add-data "sap_headers.py;." sap_converter.py
   ```

### **Usage**
1. **Extracting WAVs from SAP Files**:
   - Click the `Extract WAVs from SAP` button and select the SAP file you want to extract from.
   - Choose the folder where you want to save the extracted WAV files.

2. **Creating SAP Files from WAVs**:
   - Select the appropriate SAP category from the dropdown (e.g., Core, Door, etc.).
   - For **Voice/Music**, **Footstep**, and **Custom**, no additional file selection is needed. Just click `Create SAP from WAVs`.
   - For other categories, select the SAP file name from the dropdown and click `Create SAP from WAVs`.

3. **Warnings**:
   - The program displays a warning for "Custom" SAP types, advising the user to edit the EXE/SLUS or EDT/EDH files accordingly when using this option.

### **Contributing**
We welcome contributions! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature/fix"
   ```
4. Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request to the main repository.

### **License**
This project is licensed under the MIT License. See the LICENSE file for details.
