import unittest
from tests.test_utils import get_sample_pdf_with_labels, get_sample_pdf, get_sample_sdf, get_sample_pdf_with_extra_cols, get_sample_pdf_with_no_text_col ,get_sample_spark_dataframe
from nlu import *

class TestSentenceDetector(unittest.TestCase):

    def test_sentence_detector(self):
        pipe = nlu.load('sentence_detector', verbose=True )
        pipe.print_info()
        df = pipe.predict('HELLO WORLD! How are YOU. This is a lot of sentencessz.')
        print(df['sentence'])


if __name__ == '__main__':
    unittest.main()

