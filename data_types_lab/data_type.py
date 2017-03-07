def data_type(data):
    """ Compares and returns results based on the data type
    of the argument supplied"""
    if type(data) is str:
        return len(data)
    elif data == None:
        return 'no value'
    elif data == True or data == False:
        return data
    elif type(data) is int:
        if data < 100:
            return 'less than 100'
        elif data == 100:
            return 'equal to 100'
        else:
            return 'more than 100'
    elif type(data) is list:
        for i in range(len(data)):
            if i == 2:
                return data[i]
        else:
            return None
        
