import time


class RFID:
    def __init__(self):
        self.authenticated = False
        self.authenticatedIds = []
        self.main()

    def main(self):
        while True:
            print('RFID')
            id = self.__readId()

            if id:
                self.__searchAuthenticatedId(id)

            time.sleep(1)

    def __authenticateId(self, id):
        self.authenticated = True
        self.authenticatedIds.append(id)

    def __unAuthenticateId(self, id):
        self.authenticatedIds.remove(id)

        if len(self.authenticatedIds) == 0:
            self.authenticated = False

    def __searchAuthenticatedId(self, readId):
        if list(filter(lambda x: readId in x, self.authenticatedIds)):
            self.__unAuthenticateId(readId)

        self.__authenticateId(readId)

    def __readId(self):
        id = '918273645'
        return id


