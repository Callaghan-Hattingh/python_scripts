class Category:

    def __init__(self, category):
        self.category = category
        self.funds = 0
        self.total_income = 0
        self.ledger = []
        self.op = ''
        pass

    def deposit(self, amount, description=None):
        self.damount = amount
        self.total_income += amount
        self.ddescription = description
        if self.ddescription == None:
            self.ledger.append({'amount': (self.damount), 'description': ''})
        else:
            self.ledger.append(
                {'amount': (self.damount), 'description': (self.ddescription)})
        self.funds += self.damount

    def withdraw(self, amount, description=None):
        self.wamount = amount
        self.wdescription = description
        if self.check_funds(self.wamount):
            if self.wdescription == None:
                self.ledger.append(
                    {'amount': -(self.wamount), 'description': ''})
            else:
                self.ledger.append(
                    {'amount': -(self.wamount), 'description': (self.wdescription)})
            self.funds -= self.wamount
            return True
        else:
            return False

    def get_balance(self):
        return self.funds

    def transfer(self, amount, other_category):
        self.tamount = amount
        if self.check_funds(self.tamount):
            self.ledger.append(
                {'amount': -(self.tamount), 'description': f'Transfer to {other_category.category}'})
            self.funds -= self.tamount
            other_category.deposit(
                self.tamount, description=f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        self.cfamount = amount
        if self.funds >= self.cfamount:
            return True
        else:
            return False

    def __str__(self):
        self.op = self.category
        self.op = self.op.center(30, '*')
        for i in self.ledger:
            try:
                left = i['description'][0:23]
            except TypeError:
                left = ''
            right = i['amount']
            right = f'{right:.2f}'
            self.op += f'\n{left:<23}{right:>7}'
        self.op += f'\nTotal: {self.funds}'
        return self.op


def create_spend_chart(categories):
    total = 0
    op = 'Percentage spent by category\n'

    spent = [category.total_income-category.funds for category in categories]
    for i in spent:
        total += i
    percentage = [round(i/total*10,1) for i in spent]
    cp = [round(i) for i in percentage]
    for i in range(0,len(cp),1):
        if cp[i] > percentage[i]:
            cp[i]=cp[i]-1
    fp = [i*10 for i in cp]
    
    for i in range(100,-10,-10):
        op += f'{i}'.rjust(3) + '| '
        for percent in fp:
            if percent >= i:
                op += 'o  '
            else:
                op += '   '
        op += '\n'
     
    op += ' '*4+'-'*(len(fp)*3+1)
    op += '\n     '

    name_list = [category.category for category in categories]

    max_len_category = max([len(i) for i in name_list])

    for i in range(max_len_category):
        for name in name_list:
            if len(name)>i:
                op+= name[i] +'  '
            else:
                op+= '   '
        if i < max_len_category-1:
            op+='\n     '
    return op



