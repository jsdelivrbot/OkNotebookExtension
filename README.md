![ok](http://i.imgur.com/84czrXg.jpg?3) Editor
===============

![Demo](http://imgur.com/FmQ32Tm.gif)

Jupyter Notebook extension for editing oktests using the %ok cell magic.

To automatically install both the magic and the nbextension, run: 
```bash
curl -L https://raw.githubusercontent.com/AustenZhu/OkNotebookExtension/master/install.sh > ~/install.sh
sudo bash ~/install.sh
```
Make sure to load in the ok_magic before working with buttons: 
```python
%load_ext ok_editor
```


To manually install: 
```bash
jupyter nbextension install --user https://cdn.jsdelivr.net/gh/AustenZhu/OkNotebookExtension@master/ok_editor.js
curl -L https://cdn.jsdelivr.net/gh/AustenZhu/OkNotebookExtension@master/ok.css > $(jupyter --data-dir)/nbextensions/ok.css
```
And then follow the README in the ok_magic folder to install the magic. 


NOTE: Metadata for tests is already added into the file. Additionally, the most recent version no longer concatenates a 
```python
%%writefile
```
line. 
