class string_processor:

    def __init__(self):
        self.user_input = 0
    
    def check_all_string(self,x):
        if all(isinstance(item, str) for item in x):
            self.user_input = x
            print("from check_all_string {}".format(self.user_input))
        else:
            accept_input()

    def accept_input(self):
        while 1:
            user_input = input('Enter your Input(Please enter either a string or list of strings):')
            if isinstance(user_input,str):
                print(type(user_input))
                self.user_input = user_input
                print(self.user_input)
                break
            elif isinstance(user_input, list):
                self.check_all_string(user_input)
                break
            else:
                print("Please enter either a string or list of strings")
                
if __name__ == '__main__':
    prog = string_processor()
    prog.accept_input()
