#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension
import os
import sys


def get_rootdir():
    return os.path.dirname(__file__)
def get_includedir():
    return os.path.join(get_rootdir(), 'include')
def get_librarydir():
    return os.path.join(get_rootdir(), 'lib')


crfsuite_module = Extension(
        '_crfsuite',
        sources = [
                'swig/crfsuite.cpp',
                'swig/python/export_wrap.cpp',
                'lib/crf/src/crf1d_context.c',
                'lib/crf/src/dataset.c',
                'lib/crf/src/train_arow.c',
                'lib/crf/src/crf1d_encode.c',
                'lib/crf/src/dictionary.c',
                'lib/crf/src/train_averaged_perceptron.c',
                'lib/crf/src/crf1d_feature.c',
                'lib/crf/src/holdout.c',
                'lib/crf/src/train_l2sgd.c',
                'lib/crf/src/crf1d_model.c',
                'lib/crf/src/logging.c',
                'lib/crf/src/train_lbfgs.c',
                'lib/crf/src/crf1d_tag.c',
                'lib/crf/src/params.c',
                'lib/crf/src/train_passive_aggressive.c'
                'lib/crf/src/crfsuite.c',
                'lib/crf/src/quark.c',
                'lib/crf/src/crfsuite_train.c',
                'lib/crf/src/rumavl.c'
            ],
        swig_opts=['-c++', '-Iinclude'],
        include_dirs=['lib/cqdb/include', 'include'],
        extra_link_args=['-shared'],
        language='c++',
    )

setup(
        name = 'crfsuite',
        version = '0.12',
        author = 'Naoaki Okazaki',
        description = """CRFSuite Python module""",
        ext_modules = [crfsuite_module],
        py_modules = ["crfsuite"],
    )

