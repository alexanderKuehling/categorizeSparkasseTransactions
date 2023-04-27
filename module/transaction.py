class transaction:
    # transactions get initiated with str(row)
    def __init__(self, row):
        self.amount = None
        self.use = None
        self.date = None
        self.account = None
        self.categorie = None
        self.reciever = None
        self.row = str(row)
        self.extractProperties()
        self.returnElements()

    # extract the words and assign the transaction object properties their value
    def extractProperties(self):
        words = self.stringCutElements()
        self.account = words[0]
        self.categorie = ""
        if words[11] == " ":
            self.reciever = "Unknown"
        else:
            self.reciever = words[11]
        self.date = words[1]
        self.use = words[4]
        self.amount = words[14]

    # take the row and extract the words char by char
    # remove ",',[,]
    def stringCutElements(self):
        words = []
        word = ""
        if len(self.row) > 0:
            for i in range(0, len(self.row) - 1):
                char = self.row[i]
                if char == ";":
                    words.append(word)
                    word = ""
                elif char not in [" ", "\"", "\'", "[", "]"]:
                    word += char
            words.append(word)
        return words

    # print  all properties
    def returnElements(self):
        print(
            "Account: " + self.account + ", Categorie: " + self.categorie + ", reciever: " + self.reciever + ", date:" + self.date + ", use" + self.use + ", amount:" + self.amount)
