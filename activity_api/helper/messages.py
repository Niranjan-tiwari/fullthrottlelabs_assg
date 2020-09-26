class Message():
    MESSAGE_ID = {
        1: 'Read Successful',
        2: 'Member data not found',
        3: 'Something went wrong',
        4: ' Member Activity not found'
    }

    @classmethod
    def code(cls, code):
        return cls.MESSAGE_ID.get(code, 'Unknown')
