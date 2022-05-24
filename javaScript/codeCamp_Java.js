let catName = "Oliver"
let catSound = "Meow"
// Let vs Const; Constants are read-only and can not be reassigned
// Immutable vs Mutable

const FCC = "freeCodeCampe"; // Constants best practice is to be uppercase
let fact = "is cool!";
fact = "is awesome!";
console.log(FCC, fact);

const SUM = 10 + 10;  // 20
const differnce = 45 - 33; // 12
const product = 8 * 10; // 80
const quotient = 66 / 33; // 2

let myVar = 87;
myVar++; // same as myVar = myVar + 1

const product = 2.0 * 2.5;
const quotient = 4.4 / 2.0;

const remainder = 11 % 3; // 2 remainder 

let a = 3;
let b = 17;
let c = 12;

a += 3; // 3 + 12 = 15
b += 9; // 17 + 9 = 26
c += 7; // 12 + 7 = 19

// Strings in Java can be incased on single and double quotes 
const myStr = "I am a \"double quoted\" string inside \"double quotes.\""; // Change this line
const myStr = '<a href="http://www.example.com" target="_blank">Link</a>';

/*
    Code	Output
    \'	single quote
    \"	double quote
    \\	backslash
    \n	newline
    \r	carriage return
    \t	tab
    \b	word boundary
    \f	form feed
*/

const lastName = "Escamilla";
const lastLetterOfLastName = lastName[lastName.length - 1];
const secondToLastLetterOfLastName = lastName[lastName.length - 2]

//Arrays

const myArray = ["my string", 4];

// Nested Arrays
const stateArray = [["Alabama", 1],["Alaska", 2],["Arizona", 3]];

// Multi-dimensional Arrays

const myArray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [[10, 11, 12], 13, 14],
  ];
  
  const myData = myArray[2][1]; // 8

// Push
// Setup
const myArray = [["John", 23], ["cat", 2]];

// Only change code below this line
myArray.push(["dog", 3]);


// Pop removes the last element in an array
const myArray =[["John", 23],["cat", 2]];
const removedFromMyArray = myArray.pop();

// shift removes the very first element in an array
removedFromMyArray = myArray.shift();

// unshift adds elements to the front of the array
myArray.unshift(["Paul", 35]);

// Grocery list
const myList = [["Milk", 3.50], ["Eggs", 1.99], ["Bread", 2.99], ["Coke", 4.99], ["Ford F150 Pickup Truck", 59999.99]];

// Functions
function reusableFunction() {
  console.log("Hi World");
}

function timesFive(arg1){
  return arg1 * 5;
}

// Variable scope - local functions override global variables 
// Setup
const outerWear = "T-Shirt";

function myOutfit() {
  // Only change code below this line
  const outerWear = "sweater"
  // Only change code above this line
  return outerWear;
}

myOutfit();

// You can assign variables to returned function calls
let processed = 0;

function processArg(num) {
  return (num + 3) / 5;
}

processed = processArg(7)

const testArr = [1, 2, 3, 4, 5];

function nextInLine (arr, item){
  arr.push(item); // Add item to end of array
  
  return arr.shift(); // Return the removed first element of array
}

nextInLine(testArr, 6);

// == "Equality and forces type conversion"
// === strict interpritation 

//Comparison
function testGreaterOrEqual(val) {
  if (val >= 20) {  // Change this line
    return "20 or Over";
  }

  if (val > 10) {  // Change this line
    return "10 or Over";
  }

  return "Less than 10";
}

function testLogicalOr(val) {
  if(val < 10 || val > 20 ){
    return "Outside";
  }
  return "Inside";
}

testLogicalOr(15);

// Nested If's
 function testSize(num) {
  // Only change code below this line
  if (num < 5){
    return "Tiny";
  } else if (num < 10){
    return "Small";
  } else if (num < 15){
    return "Medium";
  } else if (num < 20){
    return "Large";
  } else if (num >= 20){
    return "Huge";
  }

  return "Change Me";
  // Only change code above this line
}

testSize(7);

const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];

function golfScore(par, strokes) {
  // Only change code below this line
    if(strokes == 1){
      return names[0]; // Hole-in-One!
  } else if (strokes <= par - 2 ){
    return names[1]; // Eagle
  } else if (strokes == par - 1){
    return names[2]; // Birdie
  } else if (par == strokes){
    return names[3]; // par
  }
   else if (strokes == par + 1){
    return names[4]; // Bogey
  } else if (strokes == par + 2){
    return names[5]; // Double Bogey
  } else if (strokes >= par + 3){
    return names[6]; // Go Home!
  }else

  return "Change Me";
  // Only change code above this line
}

console.log(golfScore(99, 1));
// Switch statements
function switchOfStuff(val) {
  let answer = "";
  
  switch(val){
    case "a":
      answer = "apple";
      break;
    case "b":
      answer = "bird";
      break;
    case "c":
      answer = "cat";
      break;
    default:
        answer = "stuff";
        break;
  }
  

  return answer;
}

switchOfStuff(1);

function sequentialSizes(val){
  let answer = "";

  switch(val){
    case 1:
    case 2:
    case 3:
        answer = "Low";
        break;
    case 4:
    case 5: 
    case 6: 
      answer = "Mid";
      break;
    case 7:
    case 8:
    case 9:
        answer = "High";
        break;
  }
  return answer;
}

function chainToSwitch(val){
  let answer = "";

  switch(val){
    case "bob":
      answer = "Marley";
      break;
    case 42:
      answer = "The Answer"
      break;
    case 1:
      answer = "There is no #1";
      break;
    case 99:
      answer = "Missed me by this much!";
      break;
    case 7:
      answer = "Ate Nine";
      break;
  }
}

function isLess(a, b){
  return a <= b; // Will return True if a is less then b; otherwise false 
}


// Blackjack Casino Program
let count = 0;

function cc(card){
  switch(card){
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count++;
      break;
    case 7:
    case 8:
    case 9:
      count += 0;
      break;
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count -= 1;
      break;
  }

  if(count > 0){ // Bet if we know there are high value cards left
    return count + " Bet";
  } else{ // Hold if the high value cards are gone
    return count + " Hold";
  }

  return "Change Me";
}

// Objects

const myDog = {
  "name": "Hiccup",
  legs: 4,
  tails: 2,
  friends: ["Bob", "Sam", "Alex"]
}

const testObj = {
  "hat": "ballcap",
  "shirt": "jersey",
  "shoes": "cleats"
};
const hatValue = testObj.hat;
const shirtValue = testObj.shirt;

const testObj = {
  "an entree": "hamburger",
  "my side": "veggies",
  "the drink": "water"
};

const entreeValue = testObj["an entree"]; // hamburger
const drinkValue = testObj["the drink"]; // water

const testObj = {
  12: "Namath",
  16: "Montana",
  19: "Unitas"
};

const playerNumber = 16;
const player = testObj[playerNumber];

const myDog = {
  "name": "Camper",
  "legs": 4,
  "tails": 1,
  "friends": ["everything"]
}

myDog.name = "Happy Camper";

myDog.bark = "woof"; // Add properties to class
delete myDog.bark; // delete properties 

function phoneticLookup(val) {
  let result = ""; // initialize result
  // Key/Value Dictionary
  const lookup = {
    "alpha": "Adams",
    "bravo": "Boston",
    "charlie": "Chicago",
    "delta" : "Denver",
    "echo" : "Easy",
    "foxtrot" : "Frank"
  }

  result = lookup[val]; // set result to the dictionary match and return 
  return result;
}

function checkObj(obj, checkProp){
  if (obj.hasOwnProperty(checkProp))
    return obj.checkProp; // if property exists, return it
  else
    return "Not Found";
}

checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "gift")

// Data Structure

const myMusic = [
  // Albums
  {
    "artist" : "Billy Joel",
    "title" : "Piano Man",
    "release_year" : 1973,
    "formats" : [
      "CD",
      "8T",
      "LP"
    ],
    "gold" : true
  },

  {
    "artist" : "Takanaka Masayoshi",
    "title" : "Brasilian Skies",
    "release_year" : 1973,
    "formats" : [
      "CD",
      "Vinyl",
      "MP3",
      "MP4"
    ],
    "gold" : false

  }

];


const myStorage = {
  "car": {
    "inside": {
      "glove box": "maps",
      "passenger seat": "crumbs"
     },
    "outside": {
      "trunk": "jack"
    }
  }
};

const gloveBoxContents = myStorage.car.inside["glove box"];


const myPlants = [
  {
    type: "flowers",
    list: [
      "rose",
      "tulip",
      "dandelion"
    ]
  },
  {
    type: "trees",
    list: [
      "fir",
      "pine",
      "birch"
    ]
  }
];

const secondTree = myPlants[1].list[2]; // "Pine"

// Record Collection

const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks : ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};

function updateRecords(records, id, prop, value) {
  // If prop is tracks but the album doesn't have a tracks property, create an empty array and add value to it.
  if (prop === 'tracks' && !(records[id].tracks)) {
    records[id].tracks = [];
  }
  // If prop is tracks and value isn't an empty string, add value to the end of the album's existing tracks array.
  if (prop === 'tracks' && value !== ''){
    records[id].tracks.push(value);
  // If prop isn't tracks and value isn't an empty string, update or set that album's prop to value.
  } else if (prop !== 'tracks' && value !==''){
    records[id][prop] = value;
  } else if(value === ''){
    // If value is an empty string, delete the given prop property from the album
    delete records[id][prop];
  }
  console.log(records);
  return records;
}

updateRecords(recordCollection, 5439, 'artist', 'ABBA');
updateRecords(recordCollection, 2548, "artist", "")
updateRecords(recordCollection, 1245, "tracks", "Addicted to Love")
updateRecords(recordCollection, 2468, "tracks", "Free")
updateRecords(recordCollection, 2548, "tracks", "")
updateRecords(recordCollection, 1245, "albumTitle", "Riptide")


 // Loops

 const myArray = [];
let i = 5;
 while(i >= 0 ) {
   myArray.push(i);
   i--;
 } // [5,4,3,2,1,0
for(let i = 1; i <= 5; i++){
  myArray.push(i);
} // [1,2,3,4,5]

for(let i = 1; i <= 9, i += 2;){
  myArray.push(i);
}
// Push odd numbers backwards 
for(let i = 9; i > 0; i -= 2){
  myArray.push(i);
}

// Print an array 
const myArr = [2,3,4,5,6];

for(let i = 0; i < myArray.length; i++){
  console.log(myArr[i]);
}

// Add numbers in an array
let total = 0;
for(let i = 0; i < myArr.length; i++){
  total += myArr[i];
}
console.log(total);

// Print a multi-dimensional array (matrix)
const arr = [
  [1,2]
  [3,4]
  [5,6]
]

for(let i = 0; i < arr.length; i++){
  for(let j = 0; j < arr[i].length; j++){
    console.log(arr[i][j]);
  }
}

// Multiply a matrix
function multiplyAll(arr){
  let product = 1;

  for(let i = 0; i < arr.length; i++){
    for(let j = 0; j < arr[i].length; j++){
      product *= arr[i][j]
    }
  }
}

multiplyAll([
  [1,2]
  [3,4]
  [5,6]
])

// Do While Loops
const myArray = [];
let i = 10;
// Push only the number 10 to myArray
do{
  myArray.push(i);
  i++;
} while (i <= 10);

// Recursion 
// Return the sum of the first n elements of an array
function sum(arr, n){
  let total = 0;

  if (n <= 0){
    return total; // Base case
  } else {
    return sum(arr, n-1) + arr[n - 1];
  }

}

// Profile Lookup
// Setup
const contacts = [
  {
    firstName: "Akira",
    lastName: "Laine",
    number: "0543236543",
    likes: ["Pizza", "Coding", "Brownie Points"],
  },
  {
    firstName: "Harry",
    lastName: "Potter",
    number: "0994372684",
    likes: ["Hogwarts", "Magic", "Hagrid"],
  },
  {
    firstName: "Sherlock",
    lastName: "Holmes",
    number: "0487345643",
    likes: ["Intriguing Cases", "Violin"],
  },
  {
    firstName: "Kristian",
    lastName: "Vos",
    number: "unknown",
    likes: ["JavaScript", "Gaming", "Foxes"],
  },
];

function lookUpProfile(name, prop){
  if(name === ''){
    return "No such contact";
  }
  for(let i = 0; i <= contacts.length; i++){
    if(contacts[i].firstName === name){
      //console.log(contacts[i].firstName)
      return contacts[i][prop];
    }
  }

  return "No such contact";
}

lookUpProfile("Akira", "likes");

// Random numbers

// Returns a random whole number between 1 & 9
function randomWholeNum(){

  return Math.floor(Math.random() * 10);
}

// Return a random whole number between the range specified
function randomRange(myMin, myMax){
  let product = 0;
  product = Math.floor(Math.random() * (myMax - myMin + 1)) + myMin;
  return product;
}

// Parsing

// converts a passed string to an integer
function convertToInteger(str){
  let myInt = 0;
  myInt = parseInt(str);
  return myInt;
}

// Convert binary numbers
function convertBinary(str){
  let myInt = 0;
  // overload function to set Radix to binary 
  myInt = parseInt(str, 2);
  return myInt;
}

// Conditional (Ternary) Operations

// check if two numbers are equal
function checkEqual(a, b){
  return a == b ? "Equal" : "Not Equal" 
}

// check to see if a number is positive, negative, or zero
function checkSign(num){
  return num == 0 ? "zero"
    : (num < 0) ? "negative"
    : "positive";
}

// Recursive countdown

function countdown(n){
  // Base case
  if (n < 1){
    return [];
  // Recursive call 
  } else {
    // start the countdown and push the value to the front of the list
    const arrayCount = countdown(n - 1);
    arrayCount.unshift(n);
    return arrayCount;
  }
}

function rangeOfNumbers(startNum, endNum){
  if (startNum > endNum){
    return [];
  } else {
    const myRangeArray = rangeOfNumbers(startNum + 1, endNum);
    myRangeArray.unshift(startNum + 1)
    return myRangeArray;
  }
}