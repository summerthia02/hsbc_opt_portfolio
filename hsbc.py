import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("APPENDIX DATA.xlsx", sheet_name="ReturnData")

risk_free_rate =0.04
df['Sharpe Ratio'] = (df['Expected Return'] - risk_free_rate) / df['Expected Volatility']
df = df.sort_values(by='Sharpe Ratio', ascending=False)
# Plot histogram of Sharpe Ratios
plt.hist(df['Sharpe Ratio'], bins=10, color='blue', alpha=0.7)
plt.xlabel('Sharpe Ratio')
plt.ylabel('Frequency')
plt.title('Histogram of Sharpe Ratios')
plt.show()

