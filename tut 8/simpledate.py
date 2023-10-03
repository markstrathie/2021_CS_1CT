import datetime

def currentday():
    return datetime.datetime.now().day

def currentmonth():
    return datetime.datetime.now().month

def currentyear():
    return datetime.datetime.now().year

def currenthour():
    return datetime.datetime.now().hour

def birthday( day, month ):
    if day == currentday() and month == currentmonth():
        return True
    else:
        return False

if birthday( 25, 11 ) == True:
    print( "happy bday" )
else:
    print( "not today")
