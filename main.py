import argparse
import sys
from datetime import datetime

import logger
from fractal_generator import FractalGenerator


def main(args):
    """Perform a main workflow:
    1) Open and load info from json file
    2) Perform IFS simulation
    3) Plot the results and save them in the file
    :param args:
    :return:
    """
    fractal_generator = FractalGenerator.initialize_from_file(args.meta_data_json)
    fractal_generator.generate_fractal(args.output_path)


def get_arguments():
    generate_fractal_parser = argparse.ArgumentParser(description="Command line tool that generates Fractals")
    generate_fractal_parser.add_argument('meta_data_json',
                                         action='store',
                                         help='Path to a file containing json data',
                                         default=8)
    generate_fractal_parser.add_argument('output_path',
                                         action='store',
                                         help='Specifies how many times IFS algorithm will be run.',
                                         default=20)
    generate_fractal_parser.add_argument('--log_level',
                                         action='store',
                                         choices=['DEBUG', 'INFO', 'ERROR'],
                                         help='Choose log level',
                                         default='INFO')
    return generate_fractal_parser.parse_args()

if __name__ == '__main__':
    try:
        start_time = datetime.now()

        arguments = get_arguments()
        logger.set_log_level(arguments.log_level)
        logger = logger.Logger(__name__)
        logger.debug(start_time)
        logger.info("Fractalator execution started with input arguments [%s]." % arguments)

        main(arguments)

        finish_time = datetime.now()
        logger.debug('Execution time: {time}.'.format(time=(finish_time - start_time)))
        logger.info('Fractalator ended successfully.')
        sys.exit(0)

    except KeyboardInterrupt as e:  # Ctrl-C
        raise e

    except SystemExit as e:  # sys.exit()
        raise e
