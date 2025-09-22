# Red [picoCTF]

## Description
In this task we were given a disk image and were supposed to find the flag.

## Approach

1. First, I ran created a working copy of the disk image.

2. Then, I mounted the image.

3. Finally search the the loop device for the flag.

## Steps
- Check the file
```bash
ale@ale:~/Documents/Cybersecurity-Writeups/picoCTF/red$ file red.png 
red.png: PNG image data, 128 x 128, 8-bit/color RGBA, non-interlaced
```

- Opening the image just showed a red image:

![png](red.png)

- Check the metadata using `exiftool`:
```bash
ale@ale:~/Documents/Cybersecurity-Writeups/picoCTF/red$ exiftool red.png 
ExifTool Version Number         : 12.40
File Name                       : red.png
Directory                       : .
File Size                       : 796 bytes
File Modification Date/Time     : 2025:09:22 14:27:46+02:00
File Access Date/Time           : 2025:09:22 14:28:34+02:00
File Inode Change Date/Time     : 2025:09:22 14:27:54+02:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 128
Image Height                    : 128
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
Image Size                      : 128x128
Megapixels                      : 0.016
```

This revealed a hidden poem:
```text 
Crimson heart, vibrant and bold, 
Hearts flutter at your sight. 
Evenings glow softly red, 
Cherries burst with sweet life. 
Kisses linger with your warmth. 
Love deep as merlot. 
Scarlet leaves falling softly, 
Bold in every stroke.
```

Upon closer inspection, I noticed that the first letters of each line spells out the message `CHECKLSB, suggesting that the flag might be hidden using **Least Significant Bit Steganography**

- Use `zsteg`to :
```bash
ale@ale:~/Documents/Cybersecurity-Writeups/picoCTF/red$ zsteg red.png 
meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="
b1,rgba,msb,xy      .. file: OpenPGP Public Key
b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
b2,bgr,msb,xy       .. file: OpenPGP Public Key
b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
b2,rgba,msb,xy      .. text: "CIkiiiII"
b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
b2,abgr,msb,xy      .. text: "iiiaakikk"
b3,rgba,msb,xy      .. text: "#wb#wp#7p"
b3,abgr,msb,xy      .. text: "7r'wb#7p"
b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped
```

Here the text seems to be encoded in **Base64** repeatedly `cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGl`

- Decode the **Base64** encoded text:
```bash
ale@ale:~/Documents/Cybersecurity-Writeups/picoCTF/red$ echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```
## Solution
**Flag**: `picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}`
