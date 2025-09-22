# Verify [picoCTF]

## Description
In this task we run a challenge instance where we find a decrypt script, a text file with a **sha256** hash and a directory containing multiple encrypted files. The task asked us to identify the file that matches the given hash value and decrypt it using the given script.

## Approach

1. First, I connected to the challenge instance via ssh.

2. Read the checksum from the `checksum.txt`file.

3. Search the file that matches the **sha256** value.

## Steps
- Connect to the challenge instance via ssh and the given password:
```bash
ssh -p 63420 ctf-player@rhea.picoctf.net
```

- Read the checksum:
```bash
ctf-player@pico-chall$ cat checksum.txt 
03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
```

- Use `find` to identify the file that we need to decrypt:
```bash
find files/ -type f -exec sha256sum {} + | grep -i '03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8'
```
The `-f` parameter is used to specify that we are looking for the type **file**. `-exec` specifies that we want to run the `sha256sum`command. We do that with the `{}` (placeholder for filename) and `+` which tells `find` to pass multiple files at once to `sha256sum. We pipe the output of `sha256sum` into grep which searches for the provided hash in a case-insensitive way (because of -i). This filters the results to show only the files whose SHA-256 hash matches the given hash and results in:
```bash
ctf-player@pico-chall$ find files/ -type f -exec sha256sum {} + | grep -i '03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8'
03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8  files/00011a60
```

-Decrypt file `00011a60` using the provided script `decrypt.sh`:
```bash
ctf-player@pico-chall$ ./decrypt.sh files/00011a60 
picoCTF{trust_but_verify_00011a60}
```
## Solution
**Flag**: `picoCTF{trust_but_verify_00011a60}`
