import sys
import pandas as pd


freq_file = sys.argv[1]
merged_file = sys.argv[2]
output_file = sys.argv[3]


freq_data = pd.read_csv(freq_file, sep='\t', header=None, names=['length', 'frequency'])
ref_data = pd.read_csv('data/reference.hist', sep='\t', header=None, names=['length', 'norm_freq'])


max_norm_freq = ref_data['norm_freq'].max()
target_length = ref_data.loc[ref_data['norm_freq'] == max_norm_freq, 'length'].values[0]
target_frequency = freq_data.loc[freq_data['length'] == target_length, 'frequency'].values[0]


required_lines = {
    length: round((norm_freq / max_norm_freq) * target_frequency)
    for length, norm_freq in zip(ref_data['length'], ref_data['norm_freq'])
    if length in freq_data['length'].values
}


extracted_lines = []
with open(merged_file, 'r') as infile:
    for line in infile:
        start, end = map(int, line.split()[1:3])
        length = end - start
        if required_lines.get(length, 0) > 0:
            extracted_lines.append(line)
            required_lines[length] -= 1


with open(output_file, 'w') as outfile:
    outfile.writelines(extracted_lines)

