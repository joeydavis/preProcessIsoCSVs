# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:35:43 2013

@author: jhdavis
"""
import sys
import qMS

if __name__ == '__main__':
    try:
        isoPath = sys.argv[1]
        p = qMS.boolParse(sys.argv[2])
        genPlots = False
        if len(sys.argv) == 4:
            genPlots = qMS.boolParse(sys.argv[3])
    except IndexError:
        errMsg = "Invalid input! include the full path to the file to be read as well as\n"
        errMsg = errMsg + "T/F for pulse sample. Optionally include T/F to output plot data"
        sys.exit(errMsg)
    dataFrame = qMS.preProcessIsoCSV(isoPath, p, genPlots)