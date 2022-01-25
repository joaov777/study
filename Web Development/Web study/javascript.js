

var names = []
var checkAppOption = prompt("Would you like to start the app? (y/n")

if(checkAppOption === "n" || checkAppOption === "N") {
    alert("bye!!")
}
else {
    
    while(actionByUser !== "quit"){

        var actionByUser = prompt("Please, select an action: add, remove, display or quit")
        if (actionByUser === "add") {
            nameByUser = prompt("What name would you like to add?")
            names.push(nameByUser)
        } else if (actionByUser === "remove") {
            nameByUser = prompt("What name would you like to remove?")
            for (let index = 0; index < names.length; index++) {
                if(names[index] === nameByUser){
                    names.splice(index,1)
                }
            }        
        } else if (actionByUser === "display") {
            console.log(names)
        } else {
            alert("You have just quitted!!")
            break
        }

    }   
}