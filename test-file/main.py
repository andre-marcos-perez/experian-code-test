from User import User
from pyspark.sql import SparkSession


def main():

    FILENAME1 = "list1.csv"
    FILENAME2 = "list2.csv"
    users = list()

    spark = SparkSession.builder.appName("main").getOrCreate()
    input1 = spark.read.format("csv").load(FILENAME1, header="true")
    input2 = spark.read.format("csv").load(FILENAME2, header="true")
    output = input1.join(input2, ["Name", "Age", "Email"], "inner")
    output = output.select(["Name", "Age", "Email"]).collect()
    for row in output:
        user = User(row.Name, row.Age, row.Email)
        users.append(user)

if __name__ == "__main__":
    main()
