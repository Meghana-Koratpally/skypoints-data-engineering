
{{ config(materialized='table') }}

SELECT
    MEMBER_ID,
    MEMBER_NAME,
    TIER_CODE,
    DATE_OF_BIRTH,
    ENROLLMENT_DATE,
    FLIGHT_DATE,
    MEMBER_TYPE,
    -- Calculate actual age
    DATEDIFF(YEAR, DATE_OF_BIRTH, CURRENT_DATE())
    - CASE
        WHEN DATEADD(
            YEAR,
            DATEDIFF(YEAR, DATE_OF_BIRTH, CURRENT_DATE()),
            DATE_OF_BIRTH
        ) > CURRENT_DATE()
        THEN 1
        ELSE 0
      END AS AGE,
    -- Identify stale members
    CASE
        WHEN FLIGHT_DATE IS NULL THEN 'NA'
        WHEN  DATEDIFF(DAY, FLIGHT_DATE, CURRENT_DATE()) > 90
        THEN 'Y'
        ELSE 'N'
    END AS STALE_MEMBER,
    COUNTRY,
    SOURCE_FILE,
    LOAD_TIMESTAMP
FROM {{ ref('int_member_master') }}
