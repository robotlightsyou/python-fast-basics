A continuation of the shell

----------
### MIT Missing Semester Lecture Two
----------
#### Shell Scripting

This is something I wish I would have gotten started with earlier. While not directly the most important skill for python, it's is a good tool for the programmer's bag of tricks. I recommend starting a folder and anytime you come across a monotonous repetitive task consider writing a little script to let your computer do the work.

That being said shell scripting is a little troublesome for beginners. When talking about python I mention the ease created by its syntax being more similar to spoken language than other programming languages. This is not a benefit with shell scripting, it's somewhat obtuse. It is still just a programming language, and most of the things on the python overview page are readily transferable to shell.

Let's take a look at some basic comparison operators. We're used to seeing greater than or less than written as symbols, but in shell they're written as flags, similar to how we pass arguments to commands on the command line. Take this example

```shell
my_variable = 5
if [[ $my_variable -lt 10 ]] then
    echo "my variable is less than ten:
else
    echo "my variable is greater than nine"
fi
```

As mentioned in the lecture, the $ is used to represent variables in the command line as well as shell scripting. We then see -lt as a flag meaning less than. Some other options are:﻿

* -lt -> less than
* -gt -> greater than
* -le -> less than or equal to
* -ge -> greater than or equal to
* -eq -> is equivalent to

I'm going to start recommending you not think of things as "a equals value." In most programming languages "=" is the assignment operator and "==" is the equivalence conditional. These are things that colloquially mean the same thing in spoken language but are very different things in programming, start training your brain early.

Notice also at the end of the block the inclusion of "fi". This is a common syntax for shell, though not entirely consistent. There are case statements which end with 'esac', but for loops end with 'done' instead of 'rof', which is only sometimes frustrating.

----------
#### Curly Brace Expansion {}
This is another one I'm working on using more. When I build websites for my courses there's a lot of boilerplate files and templates you generate before you even start thinking about code. Using this shortcut would be a handy to reduce the amount of steps needed to be manually executed.

----------
#### Lesson 2 Exercises:

Attempt 1 and 2. Depending on how you feel proceed, but don't get too bogged down in shell scripting yet. We haven't covered too many programming concepts, so if it's feeling challenging take a break.

----------
### The Takeaway
----------

There's a lot of good info in these lectures from MIT. The commands listed above that cover navigation and execution are the most important to feel comfortable/confident with. Scripting and some of the fancier tools are nice to be aware of, but they won't be immediately necessary. Focus on getting confident with the navigation, and pay a little attention to permissions. Those are the areas we will be interacting with directly in the near future.