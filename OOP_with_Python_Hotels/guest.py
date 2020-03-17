class Guest():

    def __init__(self, f_name, l_name, email, phone):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.phone = phone


    def get_info(self):
      print('\n\t- Guest - \nFirst Name:\t{} \nLast Name:\t{} \nEmail:\t\t{} \nPhone:\t\t{}'.format(self.first_name, self.last_name, self.email, self.phone))  