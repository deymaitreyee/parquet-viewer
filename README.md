**Parquet Data Merger and Loader**
**Overview:**

This Python script provides a simple, efficient method for loading and merging multiple .parquet data files into a single consolidated DataFrame.
It was developed for analysing time-series measurements (e.g., grid frequency or sensor data) stored in daily .parquet files.
The script automatically prompts the user to select a directory, reads all .parquet files within it, and concatenates them into one continuous dataset for downstream analysis.

**Features:**

Interactive folder selection via a GUI dialog (Tkinter)
Automatic detection and sorting of .parquet files
Robust error handling when no files are found
Efficient concatenation into a single pandas.DataFrame
Cross-platform compatibility (Linux, macOS, Windows)

**Requirements:**
Python version: Python 3.7 or higher

**Dependencies:**
Install required libraries using pip: pip install pandas numpy matplotlib pyarrow fastparquet.

**Usage Instructions:**

1. Run the script:
python merge_parquet_files.py

2. Select the folder:
A pop-up window will appear. Choose the directory containing your .parquet files (e.g., daily sensor or frequency data).

3. Processing:
The script will automatically:

4. Find all .parquet files in the folder
Sort them alphabetically
Load and concatenate them into one DataFrame

5. Result:
The final merged dataset is stored in the variable: full_data
You can then perform your preferred analysis or save it as a CSV/parquet file.
The script will merge them into one continuous DataFrame.

**Notes:**
Ensure all .parquet files share the same schema (column structure). If no files are detected, the script raises an exception: Exception: No files
Modify path = tk.askdirectory(...) if you prefer to set the path manually.

