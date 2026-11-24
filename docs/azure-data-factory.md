# SkyPoints Data Engineering – Azure Data Factory Pipeline Documentation

## 1. Project Overview

The SkyPoints Data Engineering project implements an automated data ingestion pipeline using Azure Data Factory (ADF) and Azure Data Lake Storage Gen2 (ADLS Gen2).

The pipeline is designed to process multiple source file formats, including CSV, TXT, and JSON, while incorporating file validation, conditional processing, and error handling.

## 2. Azure Services Used

| Service | Purpose |
|---|---|
| Azure Data Lake Storage Gen2 | Stores source and processed data |
| Azure Data Factory | Pipeline orchestration and execution |
| Azure Integration Runtime | Executes data movement activities |
| Managed Identity | Secure authentication to ADLS Gen2 |

## 3. Source Data Details

Storage Account: `strgskypoints`

Container: `skypoints`

Source folder structure:

```text
skypoints/
    raw/
        csv/
            USA.csv
            IND.csv
            AUS.csv
        txt/
            member_profiles_sample.txt
        json/
            redemptions_sample.json
```

### Supported File Formats

**CSV Files**
- Country-specific datasets.
- Comma-delimited records.
- Used for structured tabular ingestion.

**TXT Files**
- Member profile information.
- Pipe-delimited records.

**JSON Files**
- Redemption transaction information.
- Contains nested JSON structures.

## 4. Linked Services

### LS_ADLS_SkyPoints

Connects Azure Data Factory to the ADLS Gen2 storage account.

Authentication: System-assigned Managed Identity.

Required permission: Storage Blob Data Reader (for source reading).

Document any additional destination permissions configured in your environment.

## 5. Pipeline Implementation

Document the actual pipeline name and its activities.

The pipeline implements the following logical operations:

1. Identify source files.
2. Check whether files are available.
3. Handle empty folders.
4. Process available files using the configured activities.
5. Handle failures through the configured failure path.
6. Capture execution status and relevant error information.

### File Processing

CSV: Process country-specific CSV files.

TXT: Process pipe-delimited member profile data.

JSON: Process redemption JSON data.

### Empty Folder Handling

The pipeline checks whether files exist before executing file-processing activities.

If files are unavailable, the pipeline follows the configured empty-folder handling path instead of attempting unnecessary processing.

### Error Handling

The pipeline includes failure-handling logic for unsuccessful activities.

Document the actual error variables, failure dependencies, and logging mechanism implemented in your pipeline.

## 6. Pipeline Execution and Testing

The following scenarios were tested:

- Successful execution with available CSV files.
- Successful execution with available TXT files.
- Successful execution with available JSON files.
- Empty-folder handling.
- Failure handling for unsuccessful activities.
- Verification of pipeline execution through ADF Monitor.

Record the actual execution results and test dates.

## 7. Monitoring

Azure Data Factory Monitor is used to track:

- Pipeline execution status.
- Activity execution status.
- Execution duration.
- Failure details.
- Activity-level input and output.

## 8. Security

- Managed Identity is used for authentication.
- Access is controlled through Azure RBAC.
- Connection credentials and secrets should not be committed to GitHub.

## 9. Conclusion

The SkyPoints ADF pipeline establishes an automated ingestion workflow for multiple file formats.

The implementation demonstrates data orchestration, conditional processing, empty-folder handling, error handling, and pipeline monitoring using Azure Data Factory and ADLS Gen2.
