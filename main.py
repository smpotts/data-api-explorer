###
# This is a demo Python script that interacts with the Redshift Data API.
###
import boto3


def run_commands():
    # set up the client object to connect to the redshift data api in our region
    client = boto3.client('redshift-data', 'us-east-1')

    # executes the SQL statement against Redshift
    execute_stmt_resp = client.execute_statement(
        ClusterIdentifier='redshift-cluster-1',
        Database='dev',
        DbUser='awsuser',
        Sql='select * from demo.data_api_test'
    )
    # check out the execute statement response object
    print(execute_stmt_resp)

    # describe the statement to get metadata about the query running against Redshift
    # this is where you get the status of the query
    desc_stmt_resp = client.describe_statement(
        Id='61e30b26-8398-4aca-95d6-306ff1e7298e'
    )
    print(desc_stmt_resp)

    # get the results from the query
    # column data and records in the data response
    get_stmt_results_resp = client.get_statement_result(
        Id='61e30b26-8398-4aca-95d6-306ff1e7298e'
    )
    print(get_stmt_results_resp)


if __name__ == '__main__':
    run_commands()

