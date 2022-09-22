# Databricks notebook source
dbutils.fs.mount(
    source = "wasbs://conteneuresgi19@blobesgi19.blob.core.windows.net/conteneuresgi19",
    mount_point = "/mnt/blob-storage",
    extra_configs = {"fs.azure.account.key.blobesgi19.blob.core.windows.net": 
                     dbutils.secrets.get(scope = "secretscopedatabricks19",
                                         key = "KgpvwCikFX5OpLj7bF+fRuvvB9J9+YaF2VhiZEdKg4lZ7+jB1ziA+OBXco8Tmm9fNIJFWqZ7+Xvr+AStp6lElA==")
                    }
)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/blob-storage

# COMMAND ----------

dbutils.fs.unmount("/mnt/blob-storage")
