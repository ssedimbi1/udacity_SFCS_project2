# udacity_SFCS_project2
 Udadcity Data Streaming project 2


    How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
    We can increase the executor memory and the spark.streaming.kafka.maxRatePerPartition to increase the throughput and latency
    
    
    What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
    Running cat /proc/meminfo shows that we have more than 7GB of memory and upto 2.5GB is free. We can extend the driver and executor memroies by 1GB each and make them to 2GB instead of the default 1GB 
    spark.executor.memory
    spark.driver.memory

sources
https://knowledge.udacity.com/questions/180201
https://knowledge.udacity.com/questions/131619
https://spark.apache.org/docs/1.6.1/configuration.html
https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?#pyspark.sql.SparkSession
https://spark.apache.org/docs/latest/configuration.html
https://spark.apache.org/docs/latest/web-ui.html
https://knowledge.udacity.com/questions/123410
https://knowledge.udacity.com/questions/72289
