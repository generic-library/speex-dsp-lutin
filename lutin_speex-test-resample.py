#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "test: resample test algorithm"


def create(target):
	my_module = module.Module(__file__, 'speex-test-resample', 'BINARY')
	# add extra compilation flags :
	my_module.add_extra_compile_flags()
	# add the file to compile:
	my_module.add_src_file([
		'speex-dsp/libspeexdsp/testresample.c'
		])
	# name of the dependency
	my_module.add_module_depend('speex-dsp')
	return my_module


