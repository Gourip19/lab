from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd
data = pd.DataFrame({
 'Age': ['old', 'old', 'young', 'young'],
 'BP': ['high', 'normal', 'high', 'normal'],
 'Chol': ['high', 'high', 'normal', 'normal'],
 'HeartDisease': ['yes', 'yes', 'no', 'no']
})
model = DiscreteBayesianNetwork([
 ('Age', 'HeartDisease'),
 ('BP', 'HeartDisease'),
 ('Chol', 'HeartDisease')
])
model.fit(data, estimator=MaximumLikelihoodEstimator)
inference = VariableElimination(model)
result = inference.query(
 variables=['HeartDisease'],
 evidence={'Age': 'old', 'BP': 'high', 'Chol': 'high'}
)
print(result)