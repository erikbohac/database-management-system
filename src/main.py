"""
Main Module

This module contains the main entry point for the application.

"""


import logging
import os
from configuration_loader import *
from database_utils import connector
from database_manager import *


def main():
    # Parse command line arguments (if any)
    arguments().parse_args()

    conf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../', 'config'))

    # Load configuration from file
    conf_loader = ConfigLoader(f'{conf_path}/config.ini')
    config, name, logs = conf_loader.load_config()
    default_config = ['127.0.0.1', '3306', 'root', '', 'AUCTIONS', 3]
    log_format = '%(asctime)s - %(levelname)s - %(message)s'

    # Set up logging
    try:
        logs = logs.replace('\'', '')
        logging.basicConfig(filename=logs, level=logging.INFO, format=log_format)
    except:
        print('Invalid config log path, using default location')
        logging.basicConfig(filename='logs.log', level=logging.INFO, format=log_format)
        logging.error('Invalid config log path, using default location')
    logger = logging.getLogger(__name__)

    # Establish database connection
    connection = connector.Connector(*config[:-1], default_conf=default_config)

    # Initialize application components
    application = Application(config[len(config) - 1], logger)
    data_manager = DataManager(connection, name)
    controller = Controller()

    # Set up application components
    application.set_controller(controller)
    application.set_data_manager(data_manager)
    application.initialize_invoker()

    data_manager.set_application(application)

    # Start the application
    try:
        application.start()
    except Exception as e:
        print('\nProgram terminated..')
        logger.critical('An exception occurred in runtime: %s', e)
    except KeyboardInterrupt:
        print('\nProgram terminated..')
        logger.info('Program was closed')
    finally:
        connection.close_connection()


if __name__ == '__main__':
    main()
