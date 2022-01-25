// Javascript Objects
// Javascript Objects are made up of key-pair values in no specific order

//Creating a Javascript object named car
var car = {
    brand:"General Motors",
    model:"Cobalt",
    color:"gray",
    carAlert: function(){
        return this.brand;
    },
    carChangeColor: function(color){
        this.color = color
    },
    carNameLength: function(){
        console.log(this.model.length)
    },
    carAlert: function() {
        for (key in car) {
            alert(key)
        }
    },
    carBrandLastName: function() {
        console.log(this.brand.split(" ").pop())
    }

}




//Altering a key pair
//car["color"] = "red"

//Calling a method
//car.carNameLength()

/* Iterating through an object options
for (key in car){
    console.log(key);
}
*/