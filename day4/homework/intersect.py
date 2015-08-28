#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import sys
import numpy
import copy

def arrays_from_len_file( fname ):
    arrays = {}
    for line in open( fname ):
        fields = line.split()
        name = fields[0]
        size = int( fields[1] )
        arrays[name] = numpy.zeros( size, dtype=bool )
    return arrays

def set_bits_from_file( arrays, fname ):
    for line in open( fname ):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        arrays[ chrom ][ start : end ] = 1
    
arr = arrays_from_len_file( sys.argv[1] )
set_bits_from_file( arr, sys.argv[2] )

total = 0
any_overlap = 0
all_overlap = 0
half_overlap = 0

for line in open( sys.argv[3] ):
    fields = line.split()
    # Parse fields
    chrom = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    # Get slice
    sl = arr[chrom][start:end]
    # Aggregate
    total += 1
    any_overlap += sl.any()
    all_overlap += sl.all()
    # 50% overlap
    half_overlap += ( numpy.sum( sl ) / len( sl ) > 0.5 )
    
print "Total: %d, Any overlap: %d, All overlap: %d, Half overlapping: %d" % ( total, any_overlap, all_overlap, half_overlap )
        
    
        
        