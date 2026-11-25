
{{ config(materialized='table') }}

WITH redemption_data AS (

    SELECT *
    FROM {{ ref('stg_redemptions') }}

),

member_profile AS (

    SELECT *
    FROM {{ ref('stg_member_profiles') }}

),

enriched_redemptions AS (

    SELECT
        R.FEED_DATE,
        R.TRANSACTION_ID,
        R.TRANSACTION_DATE,
        R.MEMBER_ID,
        M.MEMBER_NAME,
        M.TIER_CODE,
        M.COUNTRY,
        M.STATE,
        M.ENROLLMENT_DATE,
        M.DATE_OF_BIRTH,
        M.IS_ACTIVE,
        R.PARTNER,
        R.STATUS,
        R.MILES_REDEEMED,
        R.SOURCE_FILE AS REDEMPTION_SOURCE_FILE,
        R.LOAD_TIMESTAMP AS REDEMPTION_LOAD_TIMESTAMP,
        M.SOURCE_FILE AS MEMBER_SOURCE_FILE,
        M.LOAD_TIMESTAMP AS MEMBER_LOAD_TIMESTAMP
    FROM redemption_data R
    INNER JOIN member_profile M
        ON R.MEMBER_ID = M.MEMBER_ID
)

SELECT *
FROM enriched_redemptions
