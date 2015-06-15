#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "Algorithm of speex codec"


def create(target):
	myModule = module.Module(__file__, 'speex-dsp', 'LIBRARY')
	# add the file to compile:
	myModule.add_src_file([
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
	# name of the dependency
	myModule.add_module_depend('z')
	myModule.compile_version_CC(1999)
	myModule.add_export_path(tools.get_current_path(__file__) + "/speex-dsp/include")
	# configure library:
	# Make use of ARM4 assembly optimizations
	#myModule.compile_flags('c', "-DARM4_ASM=1")
	# Make use of ARM5E assembly optimizations
	#myModule.compile_flags('c', "-DARM5E_ASM=1")
	# Make use of Blackfin assembly optimizations
	#myModule.compile_flags('c', "-DBFIN_ASM=1")
	# Disable all parts of the API that are using floats
	#myModule.compile_flags('c', "-DDISABLE_FLOAT_API=1")
	# Enable valgrind extra checks
	#myModule.compile_flags('c', "-DENABLE_VALGRIND=1")
	# Symbol visibility prefix */
	#define EXPORT __attribute__((visibility("default")))
	myModule.compile_flags('c', "-DEXPORT=''")
	# Debug fixed-point implementation */
	#myModule.compile_flags('c', "-DFIXED_DEBUG=1")
	# Compile as fixed-point / floating-point
	if True:
		myModule.compile_flags('c', "-DFIXED_POINT")
	else:
		myModule.compile_flags('c', "-DFLOATING_POINT")
		# Enable NEON support */
		#myModule.compile_flags('c', "-D_USE_NEON=1")
		# Enable SSE support */
		myModule.compile_flags('c', "-D_USE_SSE=1")
		# Enable SSE2 support */
		myModule.compile_flags('c', "-D_USE_SSE2=1")
	# Define to 1 if you have the <alloca.h> header file.
	myModule.compile_flags('c', "-DHAVE_ALLOCA_H=1")
	# Use FFT from OggVorbis */
	myModule.compile_flags('c', "-DUSE_SMALLFT=1")
	# Use C99 variable-size arrays */
	myModule.compile_flags('c', "-DVAR_ARRAYS=1")
	
	return myModule


