# SkyPoints Data Engineering Pipeline

## Project Overview

This project implements an end-to-end data engineering pipeline for the SkyPoints airline loyalty program.

The pipeline processes daily member profile files and partner airline mileage redemption JSON feeds, validates and transforms the data, and makes it available for country-specific reporting and analytics.

## Technology Stack

- Python
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Snowflake
- dbt
- SQL
- Git and GitHub

## Key Features

- Multi-source data ingestion
- Flat-file and JSON processing
- Data quality validation
- Data cleansing and standardization
- Snowflake Bronze, Silver and Gold layers
- Country-specific member data management
- Nested JSON flattening
- Incremental processing and audit tracking
- Automated testing

## Project Structure

- `data/` – Input, raw, processed and quarantined data
- `python/` – Python ETL modules
- `snowflake/` – Snowflake SQL scripts
- `dbt_project/` – dbt transformation models
- `azure/` – Azure Data Factory assets
- `tests/` – Automated tests
- `docs/` – Technical documentation
- `diagrams/` – Architecture diagrams

## Project Status

Phase 1: Project setup and repository initialization.
