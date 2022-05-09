
var allCells = document.querySelectorAll("td");
var clearGameButton = document.querySelector("#clearGameButton");


function clearBoard() {
    for (var i = 0; i < allCells.length; i++) {
       allCells[i].textContent = '';
    }
}

clearGameButton.addEventListener('click',clearBoard);

function updateCell() {
    if (this.textContent === '') {
        this.textContent = 'X';
    } else if (this.textContent === 'X') {
        this.textContent = "O";
    } else {
        this.textContent = '';
    }
}

for (let index = 0; index < allCells.length; index++) {
    allCells[index].addEventListener('click',updateCell)   
}

$('h1').click(function(){
    $(this).text("I was changed!!")
    
})

$('textarea').eq(0).keypress(function(){
   // $('h1').toggleClass('turnRed')
   console.log(event);
})

$('h1').on('dblclick',function(){
    $(this).toggleClass('turnRed')
    $('textarea').fadeToggle(1000)
})

