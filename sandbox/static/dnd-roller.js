/*const names = [];
const file = require('fs').readFileSync('first-names.txt', 'utf-8');
const lines = file.split('\n');
for (const line of lines) {
    names.push(line.trim());
}
*/

function roll() {
    const MAX_ROLL = 100
    const MAX_SIDES = 100
    var iter = 1
    var max = 20
    var total = 0
    var die_input = document.getElementById("die-type") // issue is it isn't picking up the die_input and roll_input values
    var roll_input = document.getElementById("roll-num")
    if (die_input.value && roll_input.value) {
        iter = parseInt(roll_input.value)
        if (iter > MAX_ROLL) {
            iter = MAX_ROLL
            alert("Too many rolls.")
        }
        max = parseInt(die_input.value)
        if (max > MAX_SIDES) {
            max = MAX_SIDES
            alert("Too many sides.")
        }
    }

    var roll_vals = []
    for (i=1; i <= iter; i++) {
        val = Math.floor(Math.random() * max) + 1
        total += val
        roll_vals.push(val)  // +1 to count from 1 not 0
    }
    console.log(roll_vals)
    document.getElementById("outputdice").innerHTML = roll_vals
    document.getElementById("totaldice").innerHTML = "Total: " + total
}
/*
function namegen() {
    var no = document.getElementById("nameno")
    var gennames = [];
    for (var i = 0; i < no; i++) {
        var x = names[Math.floor(Math.random() * names.length)];
        gennames.push(x);
    }
    document.getElementById("outputname").innerHTML = gennames;
}
*/