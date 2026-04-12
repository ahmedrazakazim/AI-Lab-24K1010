dm = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills'),
])
 
cpd_dis = TabularCPD(variable='Disease', variable_card=2, values=[[0.3], [0.7]])
 
cpd_fev = TabularCPD(
    variable='Fever', variable_card=2,
    values=[[0.9, 0.5], [0.1, 0.5]],
    evidence=['Disease'], evidence_card=[2]
)
 
cpd_cou = TabularCPD(
    variable='Cough', variable_card=2,
    values=[[0.8, 0.6], [0.2, 0.4]],
    evidence=['Disease'], evidence_card=[2]
)
 
cpd_fat = TabularCPD(
    variable='Fatigue', variable_card=2,
    values=[[0.7, 0.3], [0.3, 0.7]],
    evidence=['Disease'], evidence_card=[2]
)
 
cpd_chi = TabularCPD(
    variable='Chills', variable_card=2,
    values=[[0.6, 0.4], [0.4, 0.6]],
    evidence=['Disease'], evidence_card=[2]
)
 
dm.add_cpds(cpd_dis, cpd_fev, cpd_cou, cpd_fat, cpd_chi)
assert dm.check_model(), "Disease model invalid!"
print("\nDisease model validated successfully.")
 
di = VariableElimination(dm)
 
q1 = di.query(variables=['Disease'], evidence={'Fever': 0, 'Cough': 0})
print("\nInference Task 1 - P(Disease | Fever=Yes, Cough=Yes):")
print(f"  Flu  : {q1.values[0]:.4f}")
print(f"  Cold : {q1.values[1]:.4f}")
 
q2 = di.query(variables=['Disease'], evidence={'Fever': 0, 'Cough': 0, 'Chills': 0})
print("\nInference Task 2 - P(Disease | Fever=Yes, Cough=Yes, Chills=Yes):")
print(f"  Flu  : {q2.values[0]:.4f}")
print(f"  Cold : {q2.values[1]:.4f}")
 
q3 = di.query(variables=['Fatigue'], evidence={'Disease': 0})
print("\nInference Task 3 - P(Fatigue=Yes | Disease=Flu):")
print(f"  Fatigue = Yes : {q3.values[0]:.4f}")
print(f"  Fatigue = No  : {q3.values[1]:.4f}")
