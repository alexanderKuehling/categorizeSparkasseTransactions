class transaction:
    # transactions get initiated with str(row)
    def __init__(self, data ):
        self.data = data
        self.account = data[0]
        self.categorie = data[1]
        self.reciever = data[2]
        self.date = data[3]
        self.use = data[4]
        self.amount = data[5]

    # extract the words and assign the transaction object properties their value

    # print  all properties
    def returnElements(self):
        print(
            "Account: " + self.account + ", Categorie: " + self.categorie + ", reciever: " + self.reciever + ", date:" + self.date + ", use" + self.use + ", amount:" + self.amount)

    # return the properties as a string for csv files or print
    def asString(self):
        return self.account + ";" + self.categorie + ";" + self.reciever + ";" + self.date + ";" + self.use + ";" + self.amount + "\n"

    def equals(self, tr):
        if self.reciever == tr.reciever and self.date == tr.date and self.amount == tr.amount and self.use == tr.use:
            return True
        else:
            return False
