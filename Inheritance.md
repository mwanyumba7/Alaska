# Inheritance In Java 


Inheritance is a way for one class to inherit properties and methods from another class. It's like how you might inherit certain traits from your parents, like your eye color or your height.

Let's say we have a class called `Animal` that has some properties and methods that are common to all animals. We can create a new class called `Dog` that inherits from `Animal`. This means that `Dog` will have all the properties and methods of `Animal`, plus any additional properties and methods that are specific to dogs.

Here's an example code to illustrate this:

```java
class Animal {
    String name;
    int age;

    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

class Dog extends Animal {
    String breed;

    public void wagTail() {
        System.out.println("The dog wags its tail");
    }
}
```

In this example, `Dog` is a subclass of `Animal`, which means it inherits all the properties and methods of `Animal`. `Dog` also has an additional property called `breed`, and a method called `wagTail` that is specific to dogs.

Now, let's say we want to create a new class called `Poodle` that inherits from `Dog`. This means that `Poodle` will have all the properties and methods of `Dog`, plus any additional properties and methods that are specific to poodles.

Here's an example code to illustrate this:

```java
class Poodle extends Dog {
    boolean hypoallergenic;

    public void doTrick() {
        System.out.println("The poodle does a trick");
    }
}
```

In this example, `Poodle` is a subclass of `Dog`, which means it inherits all the properties and methods of `Dog`. `Poodle` also has an additional property called `hypoallergenic`, and a method called `doTrick` that is specific to poodles.

## Types Of Inheritance

There are different types of inheritance in Java:

1. Single inheritance: A subclass can only inherit from one superclass. This is the most common type of inheritance.

2. Multilevel inheritance: A subclass can inherit from a superclass, which in turn can inherit from another superclass, and so on.

3. Hierarchical inheritance: Multiple subclasses can inherit from the same superclass.

4. Multiple inheritance: A subclass can inherit from multiple superclasses. However, Java does not support multiple inheritance of classes, only multiple inheritance of interfaces.



### Single Inheritance

Single inheritance is the most common type of inheritance, where a subclass inherits from a single superclass. Here's an example:

```java
class Animal {
    String name;
    int age;

    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

class Dog extends Animal {
    String breed;

    public void wagTail() {
        System.out.println("The dog wags its tail");
    }
}
```

In this example, `Dog` is a subclass of `Animal`, which means it inherits all the properties and methods of `Animal`. `Dog` also has an additional property called `breed`, and a method called `wagTail` that is specific to dogs.

### Multilevel Inheritance

Multilevel inheritance is where a subclass inherits from a superclass, which in turn can inherit from another superclass, and so on. Here's an example:

```java
class Animal {
    String name;
    int age;

    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

class Mammal extends Animal {
    int numLegs;

    public void nurseYoung() {
        System.out.println("The mammal nurses its young");
    }
}

class Dog extends Mammal {
    String breed;

    public void wagTail() {
        System.out.println("The dog wags its tail");
    }
}
```

In this example, `Dog` is a subclass of `Mammal`, which in turn is a subclass of `Animal`. This means that `Dog` inherits all the properties and methods of `Mammal` and `Animal`. `Dog` also has an additional property called `breed`, and a method called `wagTail` that is specific to dogs.

### Hierarchical Inheritance

Hierarchical inheritance is where multiple subclasses inherit from the same superclass. Here's an example:

```java
class Animal {
    String name;
    int age;

    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

class Dog extends Animal {
    String breed;

    public void wagTail() {
        System.out.println("The dog wags its tail");
    }
}

class Cat extends Animal {
    String furColor;

    public void purr() {
        System.out.println("The cat purrs");
    }
}
```

In this example, both `Dog` and `Cat` are subclasses of `Animal`, which means they both inherit all the properties and methods of `Animal`. `Dog` has an additional property called `breed`, and a method called `wagTail` that is specific to dogs. `Cat` has an additional property called `furColor`, and a method called `purr` that is specific to cats.

### Multiple Inheritance

Multiple inheritance is where a subclass inherits from multiple superclasses. However, Java does not support multiple inheritance of classes, only multiple inheritance of interfaces. Here's an example:

```java
interface Animal {
    void makeSound();
}

interface Mammal {
    void nurseYoung();
}

class Dog implements Animal, Mammal {
    String breed;

    public void makeSound() {
        System.out.println("The dog barks");
    }

    public void nurseYoung() {
        System.out.println("The dog nurses its young");
    }

    public void wagTail() {
        System.out.println("The dog wags its tail");
    }
}
```

In this example, `Dog` implements both the `Animal` and `Mammal` interfaces, which means it must provide implementations for the `makeSound` and `nurseYoung` methods. `Dog` also has an additional property called `breed`, and a method called `wagTail` that is specific to dogs.