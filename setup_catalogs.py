# Databricks notebook source
# MAGIC %sql
# MAGIC Create catalog if not exists fmcg;
# MAGIC use catalog fmcg;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA if NOT EXISTS fmcg.gold;
# MAGIC CREATE SCHEMA if NOT EXISTS fmcg.silver;
# MAGIC CREATE SCHEMA if NOT EXISTS fmcg.bronze;

# COMMAND ----------

