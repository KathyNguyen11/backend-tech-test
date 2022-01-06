## Installation

For running this program, please make sure that your machine has installed these requirements:

- **Python**: version >3.7
- **Jq** : this package used in verified script

## How to run 
- Git clone this repo into your machine: `git clone https://github.com/KathyNguyen11/backend-tech-test.git`
- Go to the folder contains this code, ex: `cd Documents/backend-tech-test`
Have 2 way to verify this program:
1. Run command line with json file input
```commandline
./run.sh timezone.json     
```
If you caused permission error, please use below command to grant permission for this file
```commandline
chmod +x run.sh 
```
2. Run script `verify-music.sh` to verify. Ex
```commandline
../verifier/verify-music.sh run.sh
```