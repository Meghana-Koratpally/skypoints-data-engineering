
{{ config(
    materialized='table',
    schema='GOLD'
) }}

WITH redemption_data AS (

    SELECT *
    FROM {{ ref('int_redemptions_enriched') }}

),

final AS (

    SELECT
        TRANSACTION_ID,
        MEMBER_ID,
        MEMBER_NAME,
        COUNTRY,
        STATE,
        TIER_CODE,
        FEED_DATE,
        TRANSACTION_DATE,
        PARTNER,
        STATUS,
        MILES_REDEEMED,
        ENROLLMENT_DATE,
        DATE_OF_BIRTH,
        IS_ACTIVE,
        REDEMPTION_SOURCE_FILE,
        REDEMPTION_LOAD_TIMESTAMP,
        MEMBER_SOURCE_FILE,
        MEMBER_LOAD_TIMESTAMP
    FROM redemption_data

)

SELECT *
FROM final
