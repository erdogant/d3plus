# %%

from d3plus import d3plus
d3 = d3plus()
df = d3.import_example('energy')
d3.heatmap(df)

# %%
from d3plus import d3plus
d3 = d3plus()
html = d3.particles('D3plus', )


# %%

# Initialize
from d3plus import d3plus
d3 = d3plus()
#
# Load example data
df = d3.import_example('bigbang')
#
# Plot
d3.heatmap(df, color=[1,1,1,2,2,2,2], cmap='Set1')
d3.node_properties

# Color on hex
d3.heatmap(df, color=['#FFF000', '#FFF000', '#FFF000', '#000FFF' , '#000FFF', '#000FFF', '#000FFF'])
d3.node_properties

