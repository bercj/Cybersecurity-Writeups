# DISKO 1 [picoCTF]

## Description
In this task we were given a disk image and were supposed to find the flag.

## Approach

1. First, I ran created a working copy of the disk image.

2. Then, I mounted the image.

3. Finally search the the loop device for the flag.

## Steps
- Create working copy of the disk image using ``dd`:
```bash
ale@ale:~/Documents/Cybersecurity-Writeups/picoCTF/disko_1$ dd if=disko-1.dd of=workingdisko-1.dd bs=512 conv=noerror,sync status=progress
102400+0 records in
102400+0 records out
52428800 bytes (52 MB, 50 MiB) copied, 0,46801 s, 112 MB/s
```

- Created a loop device for the image using `losetup:
```bash
ale@ale:~/Documents/Cybersecurity-Writeups/picoCTF/disko_1$ sudo losetup -r -f --show workingdisko-1.dd 
[sudo] password for ale: 
/dev/loop24
```

- Search for the flag using `strings`:
```bash
ale@ale:~/Documents/Cybersecurity-Writeups/picoCTF/disko_1$ sudo strings /dev/loop24 | grep 'picoCTF{'
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
```
## Solution
**Flag**: `picoCTF{1t5_ju5t_4_5tr1n9_be6031da}`
