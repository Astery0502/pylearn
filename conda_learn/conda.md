# Conda Cheat Sheet #
referred to the [conda user guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
## Environment Managing ##

### Creating, locating and updating environment
1. To create an environment:
```bash
conda create --name myenv
```
> Replace myenv with the environment name.

This creates the myenv environment in /envs/. No packages will be installed in this environment.

2. create an environment with a specific version of Python:
```bash
conda create -n myenv python=3.6
```

3. create an environment with a specific package:
```bash
conda create -n myenv scipy
```

or:

```bash
conda create -n myenv python
conda install -n myenv scipy=0.15.0
```
> Install all the programs in this environment at the same time, otherwise it can lead to dependency condlicts

To automatically install pip or another program every time a new environment is created, add the default programs to the **create_default_packages** section of your **.condarc** configuration file.   
The default packages are installed every time you create a new environment . If you do not want the default packages installed in a particular environment, use the **--no-default-packages** flag:
```bash
conda create --no-defarlt-packages -n myenv python
```
> for more info, run conda create --help

#### Creating an environment from an environment.yml file 

1. create the environment from the <kbd>environment.yml</kbd> file:

```bash
conda env create -f environment.yml
```
The first line of the <kbd>yml</kbd> sets the new environment's name, see [create the environment manully](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually)
 
2. activate the new environment: <kbd>conda activate myenv</kbd>
3. Verify that the new environment was installed correctly:
```bash
conda env list
```
you can also use <kbd>conda info -envs</kbd>.

#### Updating an environment
Update the contents of your <kbd>environment.yml</kbd> file accordingly and then run:
```bash
conda env update --prefix ./env --file environment.yml  --prune
```
> the --prune option causes conda to remove any dependencies that are no longer required from the environment

#### Specifying a location for an environment ###

```bash
conda create --prefix ./envs jupyterlab=0.35 matplotlib=3.1 numpy=1.16
```

### setting and working with your environment ###

#### cloning an existing environment
```bash
conda create --name myclone --clone myenv
```
> myclone indicates the new, myenv indicates the one copied
to verify, use the *conda list --envs* or the same *conda list -e*

#### building identical conda environments from spec file

#### Activating an environment
Two primary effects:
1. add entries to PATH for the environment
2. run any activation scripts the environment may contain  
for more detailed info about PATH and activation scripts check the [activating the environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)

to activate:
```bash
conda activate myenv
```

#### Nested activation
To retain the current environment in the PATH, you can activate the new environment using:
```bash
conda activate --stack myenv
```  

If you want to always stack from the outermost environment, which is typically the *base* environment, you can use:
```bash
conda config --set auto_stack 1
```

#### deactivating an environment
just type: *conda deactivate*  
*conda activate* with no environment spcified is better for returning to the *base*, or conda cannot work at all for the local shell  
but for the *--stack* activated env, *conda deactivate* is better

### 
