
WITH parsed_records AS (

    SELECT
        SPLIT(RAW_LINE, '|') AS RECORD_FIELDS,
        SOURCE_FILE,
        LOAD_TIMESTAMP
    FROM {{ source('skypoints_bronze', 'MEMBER_PROFILES_TXT') }}

),

detail_records AS (

    SELECT
        TRIM(RECORD_FIELDS[2]::STRING) AS MEMBER_NAME,
        TRIM(RECORD_FIELDS[3]::STRING) AS MEMBER_ID,

        TRY_TO_DATE(
            TRIM(RECORD_FIELDS[4]::STRING),
            'YYYYMMDD'
        ) AS ENROLLMENT_DATE,

        TRY_TO_DATE(
            TRIM(RECORD_FIELDS[5]::STRING),
            'YYYYMMDD'
        ) AS LAST_FLIGHT_DATE,

        UPPER(TRIM(RECORD_FIELDS[6]::STRING)) AS TIER_CODE,

        TRIM(RECORD_FIELDS[7]::STRING) AS AGENT_NAME,
        TRIM(RECORD_FIELDS[8]::STRING) AS STATE,
        UPPER(TRIM(RECORD_FIELDS[9]::STRING)) AS COUNTRY,

        TRY_TO_DATE(
            TRIM(RECORD_FIELDS[10]::STRING),
            'MMDDYYYY'
        ) AS DATE_OF_BIRTH,

        CASE
            WHEN UPPER(TRIM(RECORD_FIELDS[11]::STRING)) = 'A'
                THEN TRUE
            WHEN UPPER(TRIM(RECORD_FIELDS[11]::STRING)) = 'I'
                THEN FALSE
            ELSE NULL
        END AS IS_ACTIVE,

        SOURCE_FILE,
        LOAD_TIMESTAMP

    FROM parsed_records

    WHERE TRIM(RECORD_FIELDS[1]::STRING) = 'D'

)

SELECT * FROM detail_records
