#!/usr/bin/python

# --------------------------------------------------------------------------------------------------------------------
# Description: This program is used to Execute SQL Script on Redshift/Aurora provided in respective configuration file.
#
# Usage: execute_redshift_scripts.py -p path_of_config_file -f config.txt -d destination (redshift/aurora)
#
# Author: NorthBay Solutions (Pvt) Ltd.
# Change log
#
# When          Who         Where                       Why                                 What
# 2020-01-28    Hamza       Create separate modules     Update design pattern               Added RedshiftSQLExecutor
#                                                                                           and AuroraSQLExecutor
# 2019-12-18    Hamza       all                         Execute SQL scripts                 Initial draft
# --------------------------------------------------------------------------------------------------------------------

import argparse
import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath('.'))

from lambdas.database_manager.db_utility import DbUtility
from lambdas.database_manager.db_utility import session_decorator


class SQLExecutor:
    """
    SQL Executor class read the executable SQL script file and execute them on DB instance.
    SQL file must be error free and should be executable without any modification
    """

    def __init__(self):
        """
        Constructor of SQLExecutor Class
        """
        self.rule_repository_manager = RuleRepositoryManager()

    def parse_sql_file(self, sql_file_path):
        """
        Helper function that will read sql file path from the file specified in sql_file_path and return the sql
        written in file.

        :param sql_file_path: path of sql file that needs to execute
        :type sql_file_path: Path
        :return: sql_queries
        :rtype sql_queries: str
        """
        with open(sql_file_path) as sql_file:
            sql_queries = sql_file.read()
            return sql_queries

    def execute_sql(self, sql):
        """
        Function that will execute sql script on DB instance

        :param sql: sql that needs to execute
        :type sql: str
        """
        print("Implementation is missing in the child class")
        pass



class AuroraSQLExecutor(SQLExecutor):
    """
    SQL Executor extended class that execute the executable SQL script on aurora.
    SQL file must be error free and should be executable without any modification
    """

    def __init__(self):
        """
        Constructor of SQLExecutor Class
        """

        self.session_count = 0
        super().__init__()
        print('Getting Aurora config values from ssm')
        self._db_utility_obj = DbUtility(self.rule_repository_manager.get_system_configuration_by_key(
            "", "", 'AuroraOI', by_path=True)).instance
        self.session = self._db_utility_obj.get_session()

    def close(self):
        """
        Implementation of DB_Utility close function that closes open session
        """
        if self._db_utility_obj:
            self._db_utility_obj.close()
            self.session = None

    @session_decorator
    def execute_sql(self, sql):
        """
        Function that will execute sql script on DB instance

        :param sql: sql that needs to execute
        :type sql: str
        """
        self.session.execute(sql)


def get_args():
    """
    Return Arguments Passed on Running the Script
    :return: arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--ConfigFile", help="SQL script config file name")
    parser.add_argument("-p", "--FilePath", help="Base path of configuration file in EDL repo")
    parser.add_argument("-d", "--Destination", help="aurora/redshift")
    return parser.parse_args()


def main():
    args = get_args()
    file_path = Path(args.FilePath)  # file path till sql directory it will be used as base path from sql scripts
    file_name = args.ConfigFile  # name of file
    # Initializer sql_executor based on destination
    if args.Destination == 'aurora':
        sql_executor = AuroraSQLExecutor()
    elif args.Destination == 'redshift':
        sql_executor = RedshiftSQLExecutor()
    else:
        print("Invalid value for argument Destination")
        sys.exit(1)
    with open(file_path / file_name) as config_file:
        sql_file_path = config_file.readline().rstrip()  # read path of first sql file
        while sql_file_path:
            try:
                print("Executing: ", sql_file_path)
                sql_queries = sql_executor.parse_sql_file(file_path / sql_file_path)
                sql_executor.execute_sql(sql_queries)
            except Exception as e:
                print("{} failed to execute due to following Exception: {}".format(sql_file_path, str(e)))
            sql_file_path = config_file.readline().rstrip()  # read path of sql files in a sequence


if __name__ == "__main__":
    main()
