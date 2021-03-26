class LineMultiplication():

    def __init__(self, num1, num2, default_in=0):
        self.var1 = num1
        self.var2 = num2
        self._var3 = num1 + num2
        self.__var4 = 10
        self.default = default_in
    
    def __private_foo(self):
        return self.__var4 + self._var3

    def _hidden_foo(self):
        return 'hidden'
    
    def forced_foo(self, num: int, txt: str) -> str:
        return str(num) + txt

    def multiply(self):
        """
        Function purpose
        A long text explanation how the function is supposed to work, what it returns etc
        You can download vscode extension which helps generate some basic information
        https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
        return:
        """
        return self.var1 * self.var2
        

    def __repr__(self):
        return '({},{})'.format(self.var1, self.var2)

        # return '('+str(self.var1) + ',' + str(self.var2) + ')'
    
    def __len__(self):
        return abs(self.var1 - self.var2)

