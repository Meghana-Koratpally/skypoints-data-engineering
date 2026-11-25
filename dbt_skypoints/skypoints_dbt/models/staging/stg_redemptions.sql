
WITH source_data AS (

    SELECT
        RAW_DATA,
        SOURCE_FILE,
        LOAD_TIMESTAMP
    FROM {{ source('skypoints_bronze', 'REDEMPTIONS_JSON') }}

),

flattened_redemptions AS (

    SELECT
        TRY_TO_DATE(SRC.RAW_DATA:feed_date::STRING,'YYYYMMDD') AS FEED_DATE,
        SRC.RAW_DATA:member_id::STRING AS MEMBER_ID,
        REDEMPTION.VALUE:txn_id::STRING AS TRANSACTION_ID,
        TRY_TO_DATE(
            REDEMPTION.VALUE:txn_date::STRING,
            'YYYYMMDD'
        ) AS TRANSACTION_DATE,
        REDEMPTION.VALUE:partner::STRING AS PARTNER,
        REDEMPTION.VALUE:status::STRING AS STATUS,
        TRY_TO_NUMBER(
            REDEMPTION.VALUE:miles_redeemed::STRING
        ) AS MILES_REDEEMED,
        SRC.SOURCE_FILE,
        SRC.LOAD_TIMESTAMP
    FROM source_data SRC,
    LATERAL FLATTEN(
        INPUT => SRC.RAW_DATA:redemptions
    ) REDEMPTION

)

SELECT
    FEED_DATE,
    MEMBER_ID,
    TRANSACTION_ID,
    TRANSACTION_DATE,
    PARTNER,
    UPPER(TRIM(STATUS)) AS STATUS,
    MILES_REDEEMED,
    SOURCE_FILE,
    LOAD_TIMESTAMP
FROM flattened_redemptions
