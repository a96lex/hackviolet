def isInDatabase(search):
    if str(search) == "test":
        return True
        # return select rearch from db
    return False


def getFromDatabase(search):
    return {str(search): "something"}
