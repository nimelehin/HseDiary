class Strings:
    result = dict()

    def __init__(self):
        self.result['retry_to_login'] = "Попробуйте войти еще раз"
        self.result['new_user'] = "Welcome, new user"
        self.result['successful_login'] = "Now you can use our system"

    def get(self, input):
        return self.result.get(input, "#ERR: NO SUCH WORD")
