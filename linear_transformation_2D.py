class LinearTransformation2D(object):
    """Class that represents a single 2D transformation together with it's probability of occurring and id."""

    def __init__(self, transformation_matrix, translation_vector, probability):
        """Initializes an instance of the class that represents a single IFS transformation.
        :param transformation_matrix: 	4- element list representing a linear transformation matrix:
                                        (0    1
                                         2    3)
        :param translation_vector:      2-element list representing translation vector (0th element - x coordinate,
                                        1st element - y coordinate)
        :param probability: 			float representing a probability with which this transformation will be chosen
        """
        self.__probability = probability
        self.__translation_vector = translation_vector
        self.__transformation_matrix = transformation_matrix

    def apply_transformation(self, point_0):
        """Applies linear 2D transformation to the point in 2D space
        :param point_0: 	point in 2D space (array with 2 elements -> [x,y]) to which this transformation should
                            be applied to
        :return: 			return point in 2D space after transformation
        """
        x_current = point_0[0]  # x coordinate
        y_current = point_0[1]  # y coordinate
        x = self.__transformation_matrix[0] * x_current + self.__transformation_matrix[1] * y_current + \
            self.__translation_vector[0]
        y = self.__transformation_matrix[2] * x_current + self.__transformation_matrix[3] * y_current + \
            self.__translation_vector[1]
        return [x, y]

    @property
    def probability(self):
        return self.__probability
