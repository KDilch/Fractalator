# Fractalator
Python 2.7 command line application that generates fractals using IFS Algorithm and plots them to the output path
specified by the user.

To run the script you need numpy and pyplot.matplotlib libraries installed.

Usage:
python main.py <meta_data_json_path> <output_path>

Optional parameter:
--log_level - possible values: 'DEBUG', 'INFO', 'ERROR'

Metadata json format:
{
  "num_iter": 20000,
   "transformations":[
      {
         "linear_transformation_matrix":[
            0.5,
            0.0,
            0.0,
            0.5
         ],
         "translation_vector":[
            0.0,
            0.0
         ],
         "probability":0.333333333333
      },
      ...
   ]
}


Note: Probabilities in meta must sum up to 1. To fulfill this condition with real numbers such us 1./3 you need to
specify at least 12 significant digits.



