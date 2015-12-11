var triplets = [];
for(var i = 97; i < 121; i+=1) {
    triplets.push(String.fromCharCode(i, i+1, i+2));
}

console.log(triplets.join('|'));
tripletRe = new RegExp(triplets.join('|'))

function validPassword(pw) {
    return tripletRe.test(pw) && !/i|o|l/.test(pw) && /(.)\1.*(.)\2/.test(pw);
}

function incString(s) {
    return (parseInt(s, 36) + 1).toString(36).replace(/0/, 'a');
}

var initial = 'vzbxxyzz';
var next = incString(initial);

do {
    next = incString(next);
    //console.log(next);
} while(!validPassword(next))


console.log(next);
