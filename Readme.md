# TODO command line tool

This scripts allow to use the [Remember the milk](https://www.rememberthemilk.com/) api from the command line using your Gmail account.

## Requirements

- Gmail [account](https://mail.google.com/) 
- Remember the milk [account](https://www.rememberthemilk.com/) 
- Python 3+
- gnome-keyring libsecret-tools
```bash
$:- sudo apt install gnome-keyring libsecret-tools 
```
## Install


- Store your email password using `secret-tool`, you must create your own label and key-values
```bash
$:-  secret-tool store --label='milki gmail password' key1 value1
```

- Copy the `send.py` into your `HOME` somewhere.

- Replace in the file `send.py` :

    * line 38,*email* : put your own email.
    * line 39,*milk_user* : put your *rememeber the milk* email username
    * line 40,*store_password_query* : put the key used to store your email password.

- Create/Edit *~/.bash_aliases* and add this(**You must put the path to your local send.py**) :
```bash
todo(){
  todo_python_file=/your own path/send.py
  python3 $todo_python "$1" "$2"
}
```


- You must enable allow to **Less secure app access** [here](https://myaccount.google.com/lesssecureapps)

- After install type
```bash
$:- . ~/.bashrc 
```

## Use the script

```bash
$:- todo "Make the scripts" "make the scripts and include all the data"
```
This include in your **Remember the Milk** todo list a new *TODO*.


    