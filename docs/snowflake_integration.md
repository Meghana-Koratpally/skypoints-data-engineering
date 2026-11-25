# Phase 6 – Snowflake Integration and Bronze Ingestion

## 1. Objective

Implement an end-to-end Azure Data Factory pipeline to ingest CSV, TXT, and JSON source files from ADLS Gen2 into Snowflake Bronze tables.

## 2. Azure Resources

| Resource | Name |
|---|---|
| Resource Group | rg-skypoints-dev |
| Storage Account | strgskypoints |
| Data Factory | adf-skypoints-dev |
| ADLS Linked Service | LS_ADLS_SkyPoints |
| Snowflake Linked Service | LS_Snowflake_SkyPoints |

## 3. Snowflake Configuration

- Database: SKYPOINTS_DB
- Bronze Schema: BRONZE
- Control Schema: CONTROL
- Warehouse: SKYPOINTS_WH
- Service User: ADF_SKYPOINTS_USER
- Role: SKYPOINTS_ADF_ROLE

Key-pair authentication was configured between Azure Data Factory and Snowflake.

## 4. Source-to-Target Mapping

| Source File | Target Table | Format |
|---|---|---|
| USA.csv | USA_MEMBERS | CSV |
| IND.csv | IND_MEMBERS | CSV |
| AUS.csv | AUS_MEMBERS | CSV |
| member_profiles_sample.txt | MEMBER_PROFILES_TXT | TXT |
| redemptions_sample.json | REDEMPTIONS_JSON | JSON |

## 5. Snowflake Objects

Created:
- CSV, TXT, and JSON file formats
- External stages for each source format
- Five Bronze ingestion tables
- CONTROL.INGESTION_LOG monitoring table

## 6. Azure Data Factory Pipeline

Pipeline: PL_SkyPoints_Bronze_Ingestion

Implemented five Snowflake Script activities using the COPY INTO command.

Activities:
- SCR_Load_USA
- SCR_Load_IND
- SCR_Load_AUS
- SCR_Load_TXT
- SCR_Load_JSON

Success and failure logging activities were configured for each ingestion activity.

## 7. Error Handling and Monitoring

Created the INGESTION_LOG table to track:
- Source file
- File type
- Target table
- Execution status
- Start and end timestamps
- Error message
- ADF pipeline name
- ADF run ID

Success and failure dependency paths were configured in ADF.

Note: Failure messages currently use generic descriptions and can be enhanced to capture actual runtime error details.

## 8. Data Quality Validation

Performed:
- Bronze table record-count validation
- NULL value validation
- Duplicate record validation
- Source-to-target reconciliation

TXT file format was corrected to use FIELD_DELIMITER = NONE to ingest complete lines into RAW_LINE.

NULL values identified during TXT validation were investigated and handled.

No duplicate records were found in the five Bronze tables during validation.

## 9. Outcome

Successfully implemented an Azure Data Factory to Snowflake Bronze ingestion solution supporting CSV, TXT, and JSON files, with execution logging and data-quality validation.

## 10. Next Phase

Implement Snowflake Silver transformations using dbt, including data cleansing, standardization, testing, and incremental processing.