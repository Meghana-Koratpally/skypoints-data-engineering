# SkyPoints – Azure Data Factory File Ingestion Pipeline

## 1. Objective

Implement an Azure Data Factory (ADF) pipeline to identify and process
incoming SkyPoints CSV, TXT, and JSON files stored in Azure Data Lake
Storage Gen2 (ADLS Gen2).

The pipeline should detect available files, process supported file
types, copy the files to the processed folder, and handle missing files,
empty folders, and copy failures in a controlled manner.

## 2. Azure Resources

| Resource        | Name                |
|-----------------|---------------------|
| Resource Group  | `rg-skypoints-dev`  |
| Storage Account | `strgskypoints`     |
| Data Factory    | `adf-skypoints-dev` |
| Linked Service  | `LS_ADLS_SkyPoints` |

## 3. Datasets

| Dataset             | Purpose                       |
|---------------------|-------------------------------|
| `DS_CSV_SkyPoints`  | Source dataset for CSV files  |
| `DS_TXT_SkyPoints`  | Source dataset for TXT files  |
| `DS_JSON_SkyPoints` | Source dataset for JSON files |

Document the file format, container, directory, and parameter settings
for each dataset.

## 4. Pipeline

**Pipeline name:** `PL_SkyPoints_File_Ingestion`

The pipeline identifies incoming files in the configured ADLS Gen2
location and processes supported CSV, TXT, and JSON files. Successfully
copied files are placed in the designated processed folder.

## 5. Activities

| Activity     | Purpose                                                                                   |
|--------------|-------------------------------------------------------------------------------------------|
| Get Metadata | Retrieves folder contents or file metadata to determine which files are available.        |
| ForEach      | Iterates through the files returned by Get Metadata when the collection is not empty.     |
| Copy Data    | Copies the applicable source file to the processed folder.                                |
| If Condition | Checks whether files or folders are available before starting file-processing activities. |
| Set Variable | Stores pipeline values required for control flow or error handling.                       |
| Fail         | Fails the pipeline with an appropriate error when a required condition or activity fails. |

Add the final pipeline screenshot in the Testing Evidence section to
show how these activities are connected.

## 6. Error Handling

Document and validate the following scenarios.

### 6.1 Missing files

- Explain how the pipeline behaves when an expected file is not present.
- Confirm whether the pipeline skips the missing file or fails, based on
  the configured business requirement.
- Capture the relevant activity output or error details where
  applicable.

### 6.2 Empty folders

- Check the file list returned by Get Metadata before executing the
  ForEach activity.
- If the folder contains no files, do not execute the ForEach activity.
- Handle the empty-folder path explicitly so that the pipeline completes
  with the intended outcome rather than attempting to iterate over an
  empty or null collection.

### 6.3 Copy failures

- Configure failure handling for Copy Data activities.
- Capture useful error information in a variable where supported by the
  activity output and expression.
- Use the Fail activity when the pipeline must report an unsuccessful
  processing outcome.
- Verify the failed activity and error details in the ADF Monitor view.

Record the actual expressions, dependency conditions, and failure
messages used in the implemented pipeline here.

