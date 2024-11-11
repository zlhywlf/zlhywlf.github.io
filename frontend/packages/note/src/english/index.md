# english

```plantuml
today we're going to be learning what a type alias is
and what the benefits of using it actually are
so first of all
usually if you want to create a type alias
you can just do it directly by creating a variable that's going to hold that type
for example
you might have a tuple of type int and string
so next time you use this
you can say you have a variable of my type
and that's going to have to conform to that tuple
so we have to pass in ten and hello
if we want to avoid any warnings from our code editor
and as you know by now
typing hinting is solely for the developer
because this will not stop us from passing in the incorrect type
we can still say something such as ten and ten
the code editor might complain
but if we print this python couldn't care less about what we pass in
and actually run the wrong script there
so let's rerun that
as you can see
it's going to output ten and ten
regardless of the type that we have defined
anyway
that's a straightforward way to define a type alis
so why do they have the type alias type from the typing module
well to explain that let's create another example
so for this example I'm going to type in strings
and this time we're going to explicitly say that this is a type alias
and then we can type in list of typing string
now we can create something called people
and that can be a list of strings
and here we'll just insert james and mario
so what is different here
well at the moment nothing is different here
this is exactly the same as writing people of list of string
and is still works the exact same way
if we pass in some integers
the code editor is going to complain that we expected a different type
but now comes the moment that we've all been waiting for 
now that we understand how we can define a type alias
using the type alias type
we can actually do something that's called forward referencing
so forward referencing means that we're going to be using a type that does not exist yet
and instead of referring to strings
we're going to create a basket
and this basket is going to be a basket of fruits
and we didn't create fruit anywhere in our program
but since we define this to be of type type alias
we can now pass in a string and insert a list of type fruit
and here type alias prevents this from being considered a string
now it's actually considered a type
even is fruit does not exist just yet
although is we run this before actually creating the fruit
it's going to return to us a string
as you can see
we're getting the string of list of type fruit
and we can verify that by passing in the type
that will give us a string back
but if we actually crate this fruit
first of all that warnings going to go away
and we're going to give this an initializer
which just takes a fruit name and the self dot fruit is going to equal the fruit
and this should be of type string and second
we can now actually use that type directly in our class
for example if we create a method called create basket
which will create a basket of fruit
we can say we want to return a basket from this
although you might be asking why
didn't you just pass in a list of fruit directly
while you cannot reference your class inside your class
it's going to give you this warning
that we have an unresolved reference for type fruit
there are other workarounds for doing this
but we're just covering how
we can use type alias here
as you can see we're referring directly to list of type fruits
and that's what we're going to get back
and I just called it a basket
but you can call is whatever you want
and here we're just going to return three times
fruits with the self dot fruit inserted
so we will return a list of fruit objects
when we create that basket now down below we can create something called a banana
which will be of type fruit
and that will equal a fruit with the name of banana
and now we can also reference the basket
which will be of type basket
and if you hover over the basket
you'll see that it's a type alias for a list of type fruit
which means here we can type in something such as banana dot
create basket and that's going to create a basket from our fruits
and if we pass in anything that's not a basket
for example alist of string and I just use string 
but you gey the point
it's going to give us this warning that it expected a list of fruit
but we got a list of string instead
so let's go back to creating that basket
and next we can actually print the basket at the index of zero
and we can refer to whatever we want from that basket
for example we can get the fruit back from that basket
and when we run this
we will get that banana back
so as you can see using type alias is very nice
if you want to create a forward reference
but that's actually all I wanted to cover in today's video
do let me know what you think about this feature
in the comments section down below 
I would love to hear about it
but anyways as always
thanks for watching and I'll see you in the next video
```
