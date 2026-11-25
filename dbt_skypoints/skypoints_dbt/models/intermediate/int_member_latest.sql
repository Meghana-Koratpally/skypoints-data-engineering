
--latest record wins :
{# This model will:
1. Read all enriched member records.
2. Partition records by MEMBER_ID.
3. Rank records by LOAD_TIMESTAMP, newest first.
4. Keep only rank 1. #}

{{ config(
    materialized='table',
    schema='SILVER'
) }}

WITH RANKED_MEMBERS AS (

    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY UPPER(TRIM(MEMBER_NAME))
            ORDER BY LOAD_TIMESTAMP DESC NULLS LAST
        ) AS RN

    FROM {{ ref('int_member_enriched') }}

)

SELECT
    MEMBER_ID,
    MEMBER_NAME,
    TIER_CODE,
    DATE_OF_BIRTH,
    ENROLLMENT_DATE,
    FLIGHT_DATE,
    MEMBER_TYPE,
    AGE,
    STALE_MEMBER,
    COUNTRY,
    SOURCE_FILE,
    LOAD_TIMESTAMP
FROM RANKED_MEMBERS
WHERE RN = 1
