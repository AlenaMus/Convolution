import numpy as np
import matplotlib.pyplot as plt

# Generate sine signal
periods = 10
samples_per_period = 200
total_samples = periods * samples_per_period  # 2000 samples

# Create time vector and sine signal
t = np.linspace(0, 2 * np.pi * periods, total_samples)
signal = np.sin(t)

# Create convolution kernel (h) - 30 samples centered around sine maximum
h_length = 30
# Center the kernel around pi/2 (where sine reaches maximum = 1)
# Take samples from pi/2 - delta to pi/2 + delta
half_length = h_length / 2
t_h = np.linspace(np.pi/2 - np.pi/4, np.pi/2 + np.pi/4, h_length)
h = np.sin(t_h)

# Perform convolution
conv_result = np.convolve(signal, h, mode='same')

# Find peaks in convolution result
# Peaks are local maxima where value is greater than neighbors
peaks = []
for i in range(1, len(conv_result) - 1):
    if conv_result[i] > conv_result[i-1] and conv_result[i] > conv_result[i+1]:
        peaks.append(i)

peaks = np.array(peaks)

# Filter peaks - keep only significant ones (above threshold)
if len(peaks) > 0:
    threshold = np.max(conv_result) * 0.7  # 70% of maximum
    significant_peaks = peaks[conv_result[peaks] > threshold]
else:
    significant_peaks = peaks

print(f"Total samples: {total_samples}")
print(f"Convolution kernel length: {h_length}")
print(f"Number of peaks found: {len(significant_peaks)}")
print(f"Peak indices: {significant_peaks}")

# Plot results
fig, axes = plt.subplots(4, 1, figsize=(12, 10))

# Plot original signal
axes[0].plot(signal)
axes[0].set_title('Original Sine Signal (10 periods, 200 samples each)')
axes[0].set_xlabel('Sample Index')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True)

# Plot convolution kernel
axes[1].plot(h)
axes[1].set_title('Convolution Kernel h (30 samples)')
axes[1].set_xlabel('Sample Index')
axes[1].set_ylabel('Amplitude')
axes[1].grid(True)

# Plot convolution result
axes[2].plot(conv_result)
axes[2].set_title('Convolution Result')
axes[2].set_xlabel('Sample Index')
axes[2].set_ylabel('Convolution Value')
axes[2].grid(True)

# Plot detected peaks on original signal
axes[3].plot(signal, label='Signal')
axes[3].plot(significant_peaks, signal[significant_peaks], 'ro', 
             markersize=8, label=f'Detected Peaks ({len(significant_peaks)})')
axes[3].set_title('Detected Peaks on Original Signal')
axes[3].set_xlabel('Sample Index')
axes[3].set_ylabel('Amplitude')
axes[3].legend()
axes[3].grid(True)

plt.tight_layout()
plt.savefig('sine_peak_detection.png', dpi=150, bbox_inches='tight')
plt.show()

# Create additional visualization: Convolution values at peak locations
fig2, ax = plt.subplots(figsize=(12, 6))

# Plot convolution result values at peak indices
if len(significant_peaks) > 0:
    conv_values_at_peaks = conv_result[significant_peaks]
    ax.stem(significant_peaks, conv_values_at_peaks, basefmt=' ', linefmt='b-', markerfmt='ro')
    ax.set_xlabel('Peak Index (x-axis)', fontsize=12)
    ax.set_ylabel('Convolution Result Value (y-axis)', fontsize=12)
    ax.set_title('Convolution Result at Maximum Indexes', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    # Add value labels on each point
    for i, (idx, val) in enumerate(zip(significant_peaks, conv_values_at_peaks)):
        ax.text(idx, val, f'{idx}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('convolution_at_peaks.png', dpi=150, bbox_inches='tight')
plt.show()

# Save peak indices to file
np.savetxt('peak_indices.txt', significant_peaks, fmt='%d')
print(f"\nPeak indices saved to 'peak_indices.txt'")
print(f"Plots saved to 'sine_peak_detection.png' and 'convolution_at_peaks.png'")