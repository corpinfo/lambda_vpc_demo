# Simple VPC Lambda demo
This Lambda function is an extremely simple demo which does the following

* Downloads the Google Home page, and writes the content to a file
* Connects to a MySQL database and gets the version of the MySQL engine

The purpose of these two tasks is to test internet connectivity of the Lambda Function, and also connectivity within a VPC to private resources.

## Preparing the demo
1. Create a directory and download the content of this repo into the directory
2. install the required Python modules to the directory `pip install -r requirements.txt -t .`
3. Update the rds_config.py with valid connection details
4. zip all files ad folders `zip -r * lambda_package.zip`
4. upload the `lambda_package.zip` file to AWS Lambda