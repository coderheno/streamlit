# DNA sequence string
dna_sequence = "AGCTTAGCTA"

# Count occurrences of each nucleotide using count() method
a_count = dna_sequence.count('A')  # Count 'A'
t_count = dna_sequence.count('T')  # Count 'T'
g_count = dna_sequence.count('G')  # Count 'G'
c_count = dna_sequence.count('C')  # Count 'C'

# Calculate total length of the DNA sequence
total_length = len(dna_sequence)

# Calculate percentage of each nucleotide
a_percentage = (a_count / total_length) * 100
t_percentage = (t_count / total_length) * 100
g_percentage = (g_count / total_length) * 100
c_percentage = (c_count / total_length) * 100

# Print counts and percentages using formatted string literals (f-strings)
print(f"A: {a_count} ({a_percentage:.2f}%), T: {t_count} ({t_percentage:.2f}%), G: {g_count} ({g_percentage:.2f}%), C: {c_count} ({c_percentage:.2f}%)")
