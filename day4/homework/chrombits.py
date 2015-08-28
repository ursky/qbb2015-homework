import numpy
import copy

class ChromosomeLocationBitArrays( object ):

    def __init__( self, dicts=None, fname=None ):
        # If dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
            sizes={}
            
        
        # If fname parameter provided, initialize from file
        if fname is not None: 
            for line in open( fname ):
                fields = line.split()
                name = fields[0]
                size = int( fields[1] )
                arrays[name] = numpy.zeros( size, dtype=bool )
        self.arrays = arrays


    def set_bits_from_file( self, fname ):
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            self.arrays[ chrom ][ start : end ] = 1
            
 
            
    def Chrom_Start_End( self, fname ):
        map=[]
        
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            map.append([ chrom, start, end ])
        
        self.map=map
        #return map
            
            
            
            
            
#__________________________________________________________________   
    def compare(self,A, B, C):
        comp=[0,0,0,0,0,0,0] # (A,B,AB,C,AC,BC,ABC)
        



        for line in range (0, len(A.map)):
            chromosome=A.map[line][0]
            start=A.map[line][1]
            end=A.map[line][2]

            slB=B.arrays[chromosome][start:end]
            slC=C.arrays[chromosome][start:end]

            if slB.any()==False and slC.any()==False:
                comp[0]+=1

            if slB.any()==True and slC.any()==True:
                comp[6]+=1

            if slB.any()==True and slC.any()==False:
                comp[2]+=1

            if slB.any()==False and slC.any()==True:
                comp[4]+=1
                
                
                
                
        for line in range (0, len(B.map)):
            chromosome=B.map[line][0]
            start=B.map[line][1]
            end=B.map[line][2]

            slA=A.arrays[chromosome][start:end]
            slC=C.arrays[chromosome][start:end]

            if slA.any()==False and slC.any()==False:
                comp[1]+=1

            if slA.any()==True and slC.any()==True:
                comp[6]+=1

            if slA.any()==True and slC.any()==False:
                comp[2]+=1

            if slA.any()==False and slC.any()==True:
                comp[5]+=1
            
            
        for line in range (0, len(C.map)):
            chromosome=C.map[line][0]
            start=C.map[line][1]
            end=C.map[line][2]

            slB=B.arrays[chromosome][start:end]
            slA=A.arrays[chromosome][start:end]

            if slB.any()==False and slA.any()==False:
                comp[3]+=1

            if slB.any()==True and slA.any()==True:
                comp[6]+=1

            if slB.any()==True and slA.any()==False:
                comp[5]+=1

            if slB.any()==False and slA.any()==True:
                comp[4]+=1


        return comp
        


        

#__________________________________________________________________   


            
        
    def intersect( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
        
        
        
    def union( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
        
        
        
        
    def complement( self ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
        
        
        
        
    def copy( self ):
        return ChromosomeLocationBitArrays( 
            dicts=copy.deepcopy( self.arrays ) )
            
            
            
            
            