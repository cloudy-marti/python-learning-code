Feuille de triche Python
=========================
Dernière mise à jour: 17/03/2020


# A ne pas oublier

1. l'indentation est signifiante:
```python
if True:
    print ("Dans le if")
    print ("Toujours dans le if")
print ("Pas dans le if")
```

2. Les chaînes peuvent être entre " ou ' 
 
3. On lance le programme depuis le terminal avec `python3 helloworld.py`

4. Les commentaires suivent un #

5. Les blocs de commentaires se trouvent entre """:
```python
"""
    Bloc de commentaire
"""
```

--------------------------------------------------------------------------------
# Structure
## If then else

Syntaxe générale:
```
if test:
    ...
    ...
else:
    ...
    ...
```

Plusieurs conditions
```python
if test or test:
    ...
    ...
elif test and test:
    ...
    ...
else:
    ...
    ...
```

## Boucle `for`

> Les boucles `for` sont en fait des *pour chaque éléments*.  Ils itérerent sur
> des structures.

1. Pour la boucle for classique, utiliser `range` (plus loin):
```
  for i in range(10):   # pour i dans [0,1,...9]
    print (i)
```

2. Itérer sur une liste
```
  for element in ["Victor", "Nadime"]:
    print (element)
```

3. Itérer sur une chaîne de caractère
```
  for c in "Hello World!"       #affiche une lettre par ligne, donc 12 en tout
    print(c);
```

4. Itérer sur un fichier
```
import sys
file = open("test.txt", "w")      # On ouvre le fichier "test.txt" en écriture
for x in [2**i for i in range(11)]:  # On écrit quelquechose dedans
  file.write(str(x)+"\n")           
file.close()                           # Puis, on ferme le fichier
file = open("test.txt","r")            # Et on le réouvre en lecture
for line in file:       # Pour chaque ligne dans `file`
  print (line, end='')    # la clause `end=''` indique de ne pas revenir à 
                          # ligne à la fin.
                          # En effet, chaque ligne termine déjà par un `\n`
```

--------------------------------------------------------------------------------
# Les listes

## La fonction `range`

* `range(10)` crée la liste [0,1,...,9]
* `range(3,10)` crée la liste [3,4,...,9] 
* `range(3,10,2)` créé la liste [3,5,7,9]
* `range(10,0,-1)` crée la liste [10,9,...,2,1]


Moyen mnémotechnique:
                     `range( x,  y,  incr)`
  premier élément qui y est--^   ^     ^-- incrément
                                 |
           premier élément qui y est pas



# Les dictionnaires

> Il s'agit d'une structure indexée par des clés. Pour chaque élément, on a donc un couple clé/valeur.

## Création

```python
empty_dict = {}

dict0 = {
    'key1':'value1',
    'key2':'value2',
    ...,
    'key':'value'
}

dict1 = dict([
    ('key1', 'value1'),
    ('key2', 'value2'),
    ...
    ('key', 'value')
])
```

## Opérations

```python
## Return the value associated to 'key'
dict['key']

## Add new key/value pair
dict['new_key'] = 'new_value'

## Remove a key/value pair from a dictionnary
dict.pop('key')

## More functions at : https://realpython.com/python-dicts/
```

# Les tuples

>Il s'agit d'un tableau immutable.
>
>* Il est de taille fixe.
>* Les éléments ne peuvent etre modifiés.
>* On accède aux éléments comme avec un tableau.

## Création

```python
empty_tuple = ()

single_tuple = ('e',)

tuple1 = ('e1', 'e2', 'e3', ...)
```

## Accès aux valeurs
```python
index = 0

# get value at index :
tuple[index]

# get multiple values at index, index + 1, index + 2
tuple[index:index+2]
```

# Les listes

## Création
```python
empty_list = []

list0 = ["e1", "e2", ... , "e"]

# Elements can be of different types
list1 = ["e1", 0, 1.4, ['another', 'list']]
```

## Opérations
```python
### Add e at the end of the list
list.append("e")

### Add e at any position i
list.insert(i, "e")

### Remove last element
list.pop()

### Remove element at position i
list.pop(i)

### Another operations at : https://www.geeksforgeeks.org/python-list/
```
>* Les indices du tuple commencent par 0 ; un indice négatif signifie qu'on commence à compter à partir de la fin du tableau.
>* Un indice *i* suivi de : indique tous les indices après *i*, ce dernier inclus.

--------------------------------------------------------------------------------
# Affichage

## print()

>On peut utiliser print("str") ou print "str" pour afficher une chaine de caractères.

## Formattage

>On peut formatter une ligne avec la méthode .format() des chaines de caractères. On met {} avec l'index correspondant pour choisir les arguments de format() qui vont remplacer les accolades.

```
age=25
print("Hello World, I am {0} years old.".format(age))
```

--------------------------------------------------------------------------------

# Définition d'une fonction

## Fonctions à 1 valeur de retour

```
def func(arg1,arg2):
	"""
	TODO : implement function
	"""
	return res
```

## Fonctions à plusieurs valeurs de retour

>Ces fonctions retournent un **tuple**.

```
def func(arg1,arg2):
	"""
	TODO : implement function
	"""
	return res1,res2
```

--------------------------------------------------------------------------------

# Manipulation de fichiers

## Ouvrir un fichier

```
file = open(path_to_file, flag)
```

>Les flags sont les suivants : r, w, a, rb, wb (les derniers pour des données binaires)

## Lecture d'un fichier

```
for line in file
	for character in line
		# do something with the character
```

--------------------------------------------------------------------------------

# Paramètres

## Arguments variadiques

### *\*args*
> Permet de passer plusieurs arguments qui pourront être itérés depuis la fonction.

```python
def function(*args):
    for arg in args:
        # do something with each argument

function("e1", "e2", "e3", ...)
```

### *\*kwargs*
> Permet de passer plusieurs arguments associés à une clé qui pourront être itérés depuis la fonction.

```python
def function(**kwargs):
    for arg in kwargs.values():
        # do something with each argument

function(a="e1", b="e2", c="e3", ...)
```