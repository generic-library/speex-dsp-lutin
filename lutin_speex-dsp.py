#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "Algorithm of speex codec"


def create(target):
	my_module = module.Module(__file__, 'speex-dsp', 'LIBRARY')
	# add the file to compile:
	my_module.add_src_file([
		'speex-dsp/libspeexdsp/filterbank.c',
		'speex-dsp/libspeexdsp/resample.c',
		'speex-dsp/libspeexdsp/scal.c',
		'speex-dsp/libspeexdsp/fftwrap.c',
		'speex-dsp/libspeexdsp/jitter.c',
		'speex-dsp/libspeexdsp/mdf.c',
		'speex-dsp/libspeexdsp/preprocess.c',
		'speex-dsp/libspeexdsp/smallft.c',
		'speex-dsp/libspeexdsp/buffer.c',
		'speex-dsp/libspeexdsp/kiss_fft.c',
		'speex-dsp/libspeexdsp/kiss_fftr.c'
		])
	"""
	my_module.add_header_file([
		'speex-dsp/include/speex/filterbank.h',
		'speex-dsp/include/speex/resample.h',
		'speex-dsp/include/speex/scal.h',
		'speex-dsp/include/speex/fftwrap.h',
		'speex-dsp/include/speex/jitter.h',
		'speex-dsp/include/speex/mdf.h',
		'speex-dsp/include/speex/preprocess.h',
		'speex-dsp/include/speex/smallft.h',
		'speex-dsp/include/speex/buffer.h',
		'speex-dsp/include/speex/kiss_fft.h',
		'speex-dsp/include/speex/kiss_fftr.h'
		])
	"""
	# name of the dependency
	my_module.add_module_depend('z')
	my_module.compile_version_CC(1999)
	my_module.add_export_path(tools.get_current_path(__file__) + "/speex-dsp/include")
	# configure library:
	# Make use of ARM4 assembly optimizations
	#my_module.compile_flags('c', "-DARM4_ASM=1")
	# Make use of ARM5E assembly optimizations
	#my_module.compile_flags('c', "-DARM5E_ASM=1")
	# Make use of Blackfin assembly optimizations
	#my_module.compile_flags('c', "-DBFIN_ASM=1")
	# Disable all parts of the API that are using floats
	#my_module.compile_flags('c', "-DDISABLE_FLOAT_API=1")
	# Enable valgrind extra checks
	#my_module.compile_flags('c', "-DENABLE_VALGRIND=1")
	# Symbol visibility prefix */
	#define EXPORT __attribute__((visibility("default")))
	my_module.compile_flags('c', "-DEXPORT=''")
	# Debug fixed-point implementation */
	#my_module.compile_flags('c', "-DFIXED_DEBUG=1")
	# Compile as fixed-point / floating-point
	if True:
		my_module.compile_flags('c', "-DFIXED_POINT")
	else:
		my_module.compile_flags('c', "-DFLOATING_POINT")
		# Enable NEON support */
		#my_module.compile_flags('c', "-D_USE_NEON=1")
		# Enable SSE support */
		my_module.compile_flags('c', "-D_USE_SSE=1")
		# Enable SSE2 support */
		my_module.compile_flags('c', "-D_USE_SSE2=1")
	# Define to 1 if you have the <alloca.h> header file.
	my_module.compile_flags('c', "-DHAVE_ALLOCA_H=1")
	# Use FFT from OggVorbis */
	my_module.compile_flags('c', "-DUSE_SMALLFT=1")
	# Use C99 variable-size arrays */
	my_module.compile_flags('c', "-DVAR_ARRAYS=1")
	
	return my_module


