# Scan Surprise [picoCTF]

## Description
In this task we get a `.png` file that supposedly contains a flag. We also have access to a challenge instance directly on the picoCTF website. The task is to recover the flag from the image.

## Approach

1. First, I connected to the challenge instance using **ssh** as instructed.

2. Secondly, I opened the file with the standard image viewer of Ubuntu. The picture was a QR code.

3. I suspected that the flag might be contained within the data of the QR code.

4. To investigate further, I used **zbarimg** to decode the QR code.

## Steps
- Connect to instance:
```bash
ssh -p 53093 ctf-player@atlas.picoctf.net
```
- Decode the QR code:
```bash
ctf-player@challenge:~/drop-in$ zbarimg flag.png 
Connection Error (Failed to connect to socket /var/run/dbus/system_bus_socket: No such file or directory)
Connection Null
QR-Code:picoCTF{p33k_@_b00_b5ce2572}
scanned 1 barcode symbols from 1 images in 0 seconds
```

## Solution
**Flag**: `picoCTF{p33k_@_b00_b5ce2572}`
