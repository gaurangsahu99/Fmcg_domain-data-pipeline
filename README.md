# Fmcg_domain-data-pipeline
End-to-end data engineering pipeline for Atlikon's acquisition of Sports Bar — ingesting, processing, and transforming data across Bronze, Silver, and Gold layers with full and incremental load support.
📊 Atlikon × Sports Bar — Data Engineering Pipeline
This project implements a scalable data engineering solution built to support Atlikon's acquisition of Sports Bar, enabling unified data processing and analytics across the merged data assets.
🏗️ Architecture
Data flows through a Medallion Architecture with three layers:

Bronze — Raw ingestion of source data from S3, preserving original records

Silver — Cleaned, validated, and conformed data ready for transformation

Gold — Aggregated, business-ready data serving analytics and reporting

⚙️ Pipeline Features

Full Load — Complete historical data ingestion from S3

Incremental Load — Daily delta processing to capture and integrate newly generated data

Automated pipelines designed for reliability and scalability

☁️ Tech Stack

Source: AWS S3

Processing: [e.g. Apache Spark / Databricks.
