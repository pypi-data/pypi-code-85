import pyspark.sql.types as t
from datalakebundle.table.schema.TableSchemaGenerator import TableSchemaGenerator

schema = t.StructType(
    [
        t.StructField("FIELD1", t.IntegerType()),
        t.StructField("FIELD2", t.DoubleType()),
        t.StructField("FIELD3", t.DoubleType()),
        t.StructField(
            "STRUCT1",
            t.StructType(
                [
                    t.StructField("NESTED_FIELD1", t.StringType()),
                    t.StructField(
                        "STRUCT2",
                        t.StructType(
                            [
                                t.StructField("NESTED_FIELD2", t.StringType()),
                            ],
                        ),
                    ),
                ],
            ),
        ),
    ],
)

expected_result = """def get_schema():
    return TableSchema(
        [
            t.StructField("FIELD1", t.IntegerType()),
            t.StructField("FIELD2", t.DoubleType()),
            t.StructField("FIELD3", t.DoubleType()),
            t.StructField(
                "STRUCT1",
                t.StructType(
                    [
                        t.StructField("NESTED_FIELD1", t.StringType()),
                        t.StructField(
                            "STRUCT2",
                            t.StructType(
                                [
                                    t.StructField("NESTED_FIELD2", t.StringType()),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        ],
        # primary_key="", # INSERT PRIMARY KEY(s) HERE (OPTIONAL)
        # partition_by="" # INSERT PARTITION KEY(s) HERE (OPTIONAL)
    )
"""

assert TableSchemaGenerator().generate(schema) == expected_result
