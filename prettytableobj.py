from prettytable import PrettyTable

table = PrettyTable()

#print(table)

#table.add_row([10, 20, 30, 40])
table.add_column('Field', ['Option1', 'Option2', 'Option3', 'Option4'])
print(table)
#table.border()