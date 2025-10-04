# Convolution-based Peak Detection in a Sine Signal

This project demonstrates how to use convolution to detect peaks in a sine signal.

## How it works

The Python script `HomeEx09Convolution.py` performs the following steps:

1.  **Generates a sine signal:** A sine wave is created with 10 periods and 200 samples per period.
2.  **Creates a convolution kernel:** A smaller sine wave segment is used as a kernel for convolution.
3.  **Performs convolution:** The script convolves the main signal with the kernel. The result of the convolution will have high values at locations that match the shape of the kernel.
4.  **Finds peaks:** It identifies local maxima in the convolution result.
5.  **Filters peaks:** A threshold is applied to keep only the most significant peaks.
6.  **Visualizes results:** The script generates and saves two plots:
    *   `sine_peak_detection.png`: Shows the original signal, the kernel, the convolution result, and the detected peaks on the signal.
    *   `convolution_at_peaks.png`: A stem plot showing the convolution values at the detected peak locations.
7.  **Saves peak data:** The indices of the detected peaks are saved to `peak_indices.txt`.

## How to run

To run the script, simply execute it with Python:

```bash
python HomeEx09Convolution.py
```

This will generate the output files in the same directory.
