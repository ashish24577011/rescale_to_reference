import sys
import pandas as pd
import matplotlib.pyplot as plt

# Command-line arguments
extracted_file = sys.argv[1]
output_plot = sys.argv[2]

# Load data
extracted_data = pd.read_csv(extracted_file, sep='\t', header=None, names=['chrom', 'start', 'end'])
ref_data = pd.read_csv('data/reference.hist', sep='\t', header=None, names=['dna_length', 'norm_freq'])

# Calculate DNA lengths and their frequencies
extracted_data['dna_length'] = extracted_data['end'] - extracted_data['start']
extracted_freq = extracted_data['dna_length'].value_counts().sort_index()

# Plot settings
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot DNA length frequency from extracted file
ax[0].bar(extracted_freq.index, extracted_freq.values, color='skyblue')
ax[0].set_title('DNA Length vs Frequency (Extracted)')
ax[0].set_xlabel('DNA Length')
ax[0].set_ylabel('Frequency')

# Plot normalized frequency from reference data
ax[1].bar(ref_data['dna_length'], ref_data['norm_freq'], color='salmon')
ax[1].set_title('DNA Length vs Normalized Frequency (Reference)')
ax[1].set_xlabel('DNA Length')
ax[1].set_ylabel('Normalized Frequency')

# Save and show plot
plt.tight_layout()
plt.savefig(output_plot)
plt.show()

