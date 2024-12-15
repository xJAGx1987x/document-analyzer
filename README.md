# Document Analyzer

Document Analyzer is a Python-based tool for analyzing text files and documents. It processes various document formats, provides metrics such as word counts and readability scores, and supports exporting results.

---

## Features
- **Multi-format Support**:
  - Analyze files in `.txt`, `.docx`, `.pdf`, `.rtf`, `.odt`, and `.html` formats.
- **Comprehensive Metrics**:
  - Total words, distinct words, lexical density, syllable count, and more.
  - Readability scores (Flesch Reading Ease, Flesch-Kincaid Grade Level).
  - Punctuation analysis and sentence complexity metrics.
- **Export Results**:
  - Save analysis results to a text file.
- **Intuitive GUI**:
  - Simple and user-friendly interface built with `customtkinter`.

---

## Dependencies
The following Python libraries are required:
- `customtkinter` (for the GUI)
- `nltk` (for tokenization and stopwords)
- `PyPDF2` (for PDF file parsing)
- `pypandoc` (for `.rtf` and `.odt` file parsing)
- `textstat` (for readability scores)
- `python-docx` (for `.docx` files)
- `beautifulsoup4` (for `.html` files)

---

## Installation

### **For Developers**
1. Clone the repository:
   ```bash
   git clone https://github.com/xJAGx1987x/document-analyzer.git
   cd document-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python document_analyzer.py
   ```

### **For End-Users**
1. Download the precompiled executable from the [Releases](https://github.com/xJAGx1987x/document-analyzer/releases) page.
2. Double-click `Doc-Analyzer.exe` to run the program.
3. If troubleshooting is needed, run the executable from a terminal:
   ```cmd
   Doc-Analyzer.exe
   ```

---

## Usage
1. Launch the application.
2. Click **"Analyze a File"** to select a document.
3. View analysis results in a pop-up window.
4. Save results using the **"Save Results"** button.
5. Use **"Export Last Results"** from the main menu to save results at any time.

---

## Features in Detail
1. **Supported Formats**:
   - `.txt`: Plain text files.
   - `.docx`: Microsoft Word documents.
   - `.pdf`: Portable Document Format.
   - `.rtf`: Rich Text Format.
   - `.odt`: OpenDocument Text.
   - `.html`: HTML files (plain text extraction).

2. **Metrics Calculated**:
   - **Lexical Metrics**:
     - Total words, distinct words, lexical density.
     - Top 10 frequent words.
   - **Structural Metrics**:
     - Average word length, average sentence length.
     - Sentence length distribution (most common lengths).
   - **Readability Metrics**:
     - Flesch Reading Ease.
     - Flesch-Kincaid Grade Level.
   - **Punctuation Analysis**:
     - Counts of punctuation marks (e.g., periods, commas, exclamations).

3. **Error Handling**:
   - Handles unsupported file types and corrupted files.
   - Logs errors to `analysis.log` for debugging.

4. **Export Options**:
   - Save analysis results to a `.txt` file for later reference.

---

## Troubleshooting
If you encounter issues:
1. Ensure all dependencies are installed (for developers):
   ```bash
   pip install -r requirements.txt
   ```
2. Run the executable from a command prompt to view error messages:
   ```cmd
   Doc-Analyzer.exe
   ```
3. Check `analysis.log` for detailed error information.

---

## Development
### **Build Instructions**
To build the executable:
1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```

2. Run the following command:
   ```bash
   pyinstaller --onefile --noconsole --icon="path_to_icon.ico" ^
   --add-data "path_to_nltk_data;./nltk_data" ^
   --hidden-import "nltk" ^
   --hidden-import "PyPDF2" ^
   --hidden-import "pypandoc" ^
   --hidden-import "textstat" ^
   --hidden-import "docx" ^
   --hidden-import "bs4" ^
   --name="Document Analyzer" document_analyzer.py
   ```

3. The executable will be in the `dist` folder.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## Attribution

This project uses the following icon:

- ![Technology Icon](assets/icons8-technology-100.ico)
  ![Technology Icon](assets/icons8-technology-100.png)
  [Technology](https://icons8.com/icon/1581/electronics) icon by [Icons8](https://icons8.com)

---


---

## License

This software is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 
