import numpy as np
ucs420_aishwary = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print("Mean:", np.mean(ucs420_aishwary))
print("Median:", np.median(ucs420_aishwary))
print("Max:", np.max(ucs420_aishwary))
print("Min:", np.min(ucs420_aishwary))
print("Unique Elements:", np.unique(ucs420_aishwary))

reshaped_ucs420_aishwary = ucs420_aishwary.reshape(4, 3)
print("Reshaped Array:\n", reshaped_ucs420_aishwary)

resized_ucs420_aishwary = np.resize(ucs420_aishwary, (2, 3))
print("Resized Array:\n", resized_ucs420_aishwary)
