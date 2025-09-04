# Databricks notebook source
!pip install gensim

# COMMAND ----------

import gensim.downloader
model = gensim.downloader.load("glove-wiki-gigaword-50")
model["tower"]

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

