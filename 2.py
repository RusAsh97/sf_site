for mdopt as md

# гружу мпс
# model = gp.read('week_404_9_6.mps')
model = md.read('week_404_9_6.mps0')
# model.readParams('gurobi.prm')

# настраиваю гуроби на минимизацию
# model.ModelSense = gp.GRB.MINIMIZE

# model.optimize()

#
# print('Objective value: ', model.objVal)
# for var in model.getVars():
#    print(var.varName, ':', var.x)
