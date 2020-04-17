# https://leetcode.com/problems/utf-8-validation

class Solution:
    
    ## calculate how long is the unicode character is
        ## mask it with 1000000 if its 1, 1st bit is 1 then mask it with 01000000 and keep count. count should tell us number of bytes
        ## except for 1 byte count should be zero
    def get_byte_count(self, byte):
        shiftbit = 8-1
        mask = 1 << shiftbit
        n = 0
        while(n<=8):
            if(mask & byte):
                mask = mask >> 1
                n+=1
            else:
                break
        return n
    
    def validUtf8(self, data: List[int]) -> bool:
           
        # we will check validity of data with following rules
        # count the first n positive bits of a character 
        #   count should be 0, 2, 3 or 4 
        #   if count is 2, 3 or 4 there should be at least "count" number of bytes left in array
        #   move iteration to current+count level to check next unicode
        # this will eliminate all the cases with length issues, we don't even have to check any further if something is wrong here
        i=0
        counts=[]
        while(i<len(data)):
            count = self.get_byte_count(data[i])
            if(count not in [0,2,3,4]):
                #print('count not in valid range', count)
                return False
            if(count == 0):
                if(data[i] & (1 << (8-1))):
                    #print('first bit count is 0 but it is not 0', data[i])
                    return False
            if(i+count) > len(data):
                #print('longer byte size but not enough bytes in array ', data, i, count, len(data), data[i])
                return False
            if(count == 0):
                count+=1
            counts.append(count)            
            i+=count
        
        # if we reach to this part of code it means  the first stage is passed, now we just have to check if each unicode character is valid
        i=0
        #print(counts)
        for count in counts:
            # if count is 0 it means it is 1 byte in length
            if(count == 1):
                i+=1
                continue
                
            shiftbit = 8
            mask = 1 << (shiftbit-count-1)
            # if n+1 bit is not 0 then return False
            if(mask & data[i]):
                #print('n+1 bit is non 0',mask,counts, data[i])
                return False
            mask1 = 1 << shiftbit-1
            mask2 = 1 << (shiftbit-2)
            for j in range(1,count):
                x = data[i+j]
                if(not (x & mask1)):
                    #print(i+j, 'th first bit is not 1', data[i])
                    return False
                if(x & mask2):
                    #print(i+j, 'th second bit is not 0', data[i])
                    return False
            i+=count
        return True
 
