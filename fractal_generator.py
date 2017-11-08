import json
import os
import numpy as np
import matplotlib.pyplot as plt

from linear_transformation_2D import LinearTransformation2D
from logger import Logger


class FractalGenerator(object):
    """Class that handles fractal generation, given transformations and number of iterations."""
    def __init__(self, num_iter, *args):
        """
        :param order: number of iterations that the transformations should be randomly chosen for
        :param args:  LinearTransformation2D objects
        """
        self.__num_iter = num_iter
        self.__transformations_pool = [arg for arg in args]
        self.__X_coordinates = np.zeros(num_iter)
        self.__Y_coordinates = np.zeros(num_iter)
        self.__logger = Logger(__name__)

    def __choose_transformations_given_probabilities(self):
        """Generates an array of indices that correspond to transformation ids, the indices are chosen with given probability,
        random choice is made num_iter times."""
        self.__logger.info("Choosing transformations with given probabilities.")
        indices = np.arange(start=0, stop=len(self.__transformations_pool), step=1)
        return np.random.choice(indices, self.__num_iter, p=[arg.probability for arg in self.__transformations_pool])

    def __run_ifs_algorithm(self, random_indices_list):
        """This function does the main job - it runs IFS algorithm to find chosen points in 2D space"""
        self.__logger.info("Computing [%s] points in 2D space using IFS algorithm." % str(self.__num_iter))
        point_next = [0, 0]
        for numIter, index in enumerate(random_indices_list):
            transformation_current = self.__transformations_pool[index]
            point_current = point_next
            point_next = transformation_current.apply_transformation(point_current)
            self.__X_coordinates[numIter] = point_next[0]
            self.__Y_coordinates[numIter] = point_next[1]

    def __plot_fractal(self, output_path):
        """Plots a fractal using computed data."""
        self.__logger.info("Plotting the fractal to output_path [%s]." % os.path.abspath(output_path))
        plt.ioff()
        plt.style.use('default')
        plt.scatter(self.__X_coordinates, self.__Y_coordinates, s=0.2, c='#F98866', lw=0, marker='o')
        plt.savefig(output_path)
        plt.close()

    def generate_fractal(self, output_path):
        """Public function that glues together:
         1)Choosing random transformation indices
         2)Computing points in space given transformations and the list of indices
         3)Plotting the result to a file"""
        list_transformation_indices = self.__choose_transformations_given_probabilities()
        self.__run_ifs_algorithm(list_transformation_indices)
        self.__plot_fractal(output_path=output_path)

    @staticmethod
    def initialize_from_file(path):
        """Initializes an instance of FractalGenerator from json file.
        :param path:				        string representing json file path
        :return: fractalGenerator		    returns an instance of FractalGenerator object
        """
        if not os.path.exists(path):
            raise RuntimeError('File [%s] does not exist' % path)

        with open(path) as json_file:
            json_obj = json.load(json_file)
            if not json_obj:
                raise ValueError('Failed to load json file [%s]' % path)
            return json.loads(json_obj, cls=TransformationJSONDecoder)


class TransformationJSONDecoder(json.JSONDecoder):
    """Class reads data from json file containing transformations and their probabilities."""
    def decode(self, json_obj):
        num_iter = json_obj['num_iter']
        transformation_obj_list = []
        for entry in json_obj['transformations']:
            transformation_obj_list.append(LinearTransformation2D(transformation_matrix=entry['linear_transformation_matrix'],
                                                                  translation_vector=entry['translation_vector'],
                                                                  probability=entry['probability']))

        return FractalGenerator(num_iter, *transformation_obj_list)
