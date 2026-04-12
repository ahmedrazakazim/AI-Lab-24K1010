from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
 
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])
 
cpd_I = TabularCPD(variable='Intelligence', variable_card=2, values=[[0.7], [0.3]])
cpd_S = TabularCPD(variable='StudyHours', variable_card=2, values=[[0.6], [0.4]])
cpd_D = TabularCPD(variable='Difficulty', variable_card=2, values=[[0.4], [0.6]])
 
cpd_G = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.30, 0.70, 0.10, 0.40, 0.10, 0.40, 0.05, 0.20],
        [0.40, 0.20, 0.50, 0.40, 0.40, 0.40, 0.25, 0.50],
        [0.30, 0.10, 0.40, 0.20, 0.50, 0.20, 0.70, 0.30],
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)
 
cpd_P = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.50],
        [0.05, 0.20, 0.50],
    ],
    evidence=['Grade'],
    evidence_card=[3]
)
 
model.add_cpds(cpd_I, cpd_S, cpd_D, cpd_G, cpd_P)
assert model.check_model(), "Model is invalid!"
print("\nModel validated successfully.")
 
infer = VariableElimination(model)
 
r1 = infer.query(variables=['Pass'], evidence={'StudyHours': 0, 'Difficulty': 0})
print("\nP(Pass | StudyHours=Sufficient, Difficulty=Hard):")
print(f"  Pass = Yes : {r1.values[0]:.4f}")
print(f"  Pass = No  : {r1.values[1]:.4f}")
 
r2 = infer.query(variables=['Intelligence'], evidence={'Pass': 0})
print("\nP(Intelligence | Pass=Yes):")
print(f"  Intelligence = High : {r2.values[0]:.4f}")
print(f"  Intelligence = Low  : {r2.values[1]:.4f}")
