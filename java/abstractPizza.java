abstract class Pizza {
    String description = "Unknown Pizza";

    public String getDescription(){
        return description;
    }

    public abstract int getCost();
}

// Decorator classes 
abstract class ToppingsDecorator extends Pizza{
    public abstract String getDescription();
}

//Concrete Pizza classes
class PeppyPaneer extends Pizza{
    public PeppyPaneer() {
        description = "PeppyPaneer";
    }
    public int getCost(){
        return 100;
    }
}

class FarmHouse extends Pizza{
    public FarmHouse(){
        description = "Farmhouse";
    }

    public int getCost(){
        return 200;
    }
}

class Margherita extends Pizza{
    public Margherita(){
        description = "Margherita";
    }

    public int getCost(){
        return 2543;
    }
}

class ChickenFiesta extends Pizza{
    public ChickenFiesta(){
        description = "ChickenFiesta";
    }

    public int getCost(){
        return 199;
    }
}

class MegaMeat extends Pizza{
    public MegaMeat(){
        description = "MegaMeat";
    }

    public int getCost(){
        return 999;
    }
}

// Toppings
class FreshTomato extends ToppingsDecorator{
    Pizza pizza;

    public FreshTomato(Pizza pizza){
        this.pizza = pizza;
    }

    public String getDescription() {
        return pizza.getDescription() + ", Fresh Tomato";
    }

    public int getCost(){
        return 40 + pizza.getCost();
    }
}

class Barbeque extends ToppingsDecorator{
    Pizza pizza;
    
    public Barbeque(Pizza pizza){
        this.pizza = pizza;
    }

    public String getDescription(){
        return pizza.getDescription() + ", Barbeque";
    }

    public int getCost(){
        return 90 + pizza.getCost();
    }
}

class Anchovies extends ToppingsDecorator{
    Pizza pizza;

    public Anchovies(Pizza pizza){
        this.pizza = pizza;
    }

    public String getDescription(){
        return pizza.getDescription() + ", Anchovies";
    }

    public int getCost(){
        return 199 + pizza.getCost();
    }
}

class Pineapple extends ToppingsDecorator{
    Pizza pizza;

    public Pineapple(Pizza pizza){
        this.pizza = pizza;
    }

    public String getDescription(){
        return pizza.getDescription() + ", Pineapple";
    }

    public int getCost(){
        return 55 + pizza.getCost();
    }
}

class PizzaStore{
    public static void main(String args[]){
        Pizza pizza = new FarmHouse();
        System.out.println(pizza.getDescription() + "Cost: " + pizza.getCost());

        // create a margherita pizza
        Pizza pizza2 = new Margherita();
        // decorate it with fresh tomato toppings :)
        pizza2 = new FreshTomato(pizza2);
        // let get barbeque too
        pizza2 = new Barbeque(pizza2);
        System.out.println(pizza2.getDescription() + " Cost : " + pizza2.getCost());
    }
}