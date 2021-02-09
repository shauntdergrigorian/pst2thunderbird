# pst2thunderbird
A tool for importing PST archives into Thunderbird

## Requirements
This tool requires readpst which can be installed using the following commands:
#### Ubuntu
```sudo apt-get install readpst```

#### Arch/Manjaro
```pacman -S libpst```

You'll also need the filepath of your Thunderbird data folder. It's typically located under `~/.thunderbird/<id>/Mail/`
  
## Usage
```python3 convert.py <path_to_pst> <path to Thunderbird mail folder, typically ~/.thunderbird/XXXXX/Mail/>```

For example:

```python3 convert.py ~/Documents/John\ Doe\ Archive.pst ~/.thunderbird/ab5cdefg.default-release/Mail/```

If Thunderbird was open before running this command, close and re-open it. The new mailbox should now be available for reading and searching.
