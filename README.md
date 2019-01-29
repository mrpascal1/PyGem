# PyGem
PyGem is a python to java (source-to-source) translator.

# Experimental Release
PyGem depends highly on Regular Expression.
It matches the syntax of python and replace it with java.

# Features
1.It Can produce the method(java) from fucntion(python)
2.It can also recreate classes

# Bugs
1.Curly Braces "{ }" does not Work Properly
FOR EXAMPLE: If we create a funtion or class in python like:

<code>
    
    class HelloWorld():
        print("Hello")
    HelloWorld()

</code>
Then It will correctly produce braces
But, If we dont call the class
then it will not close the braces(similar problems with functions)

# Todo:
1. Auto-Generate Main Method.
2. Create object of classes and Call them.
3. Proper variable Declaration.


# Compiler Fronted in Python
Along With this I am Also Working on a Compiler Fronted to generate an intermediate code in python
so it can be easily converted into any other language
