{{ config(
    materialized='table',
    schema='GOLD'
) }}

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
FROM {{ ref('int_member_latest') }}
WHERE UPPER(TRIM(COUNTRY))
    IN ('AUS', 'AU', 'AUSTRALIA')