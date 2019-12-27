import copy
from intcode_computer import IntcodeComputer

inputFile = 'input/merry_xmas'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data
    
    
    
if __name__ == "__main__":
	prg = getInputData()
	#print(prg)
	IC = IntcodeComputer(prg)
	IC.run_program()
	str = ""
	str = str.join(([chr(ch) for ch in IC._output]))
	print(str)


'''
       .     .                       *** **
                !      .           ._*.                       .
             - -*- -       .-'-.   !  !     .
    .    .      *       .-' .-. '-.!  !             .              .
               ***   .-' .-'   '-. '-.!    .
       *       ***.-' .-'         '-. '-.                   .
       *      ***$*.-'               '-. '-.     *
  *   ***     * ***     ___________     !-..!-.  *     *         *    *
  *   ***    **$** *   !__!__!__!__!    !    !  ***   ***    .   *   ***
 *** ****    * *****   !__!__!__!__!    !      .***-.-*** *     *** * #_
**********  * ****$ *  !__!__!__!__!    !-..--'*****   # '*-..---# ***
**** *****  * $** ***      .            !      *****     ***       ***
************ ***** ***-..-' -.._________!     *******    ***      *****
***********   .-#.-'           '-.-''-..!     *******   ****...     #
  # ''-.---''                           '-....---#..--'****** ''-.---''-
                  Merry Christmas
                  ~RudolphPlays~
'''
   
   