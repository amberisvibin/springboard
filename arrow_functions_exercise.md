
# Arrow Functions Exercise

In this exercise, you’ll refactor some ES5 code into ES2015.

## ES5 Map Callback

```js
function double(arr) {
	return arr.map(function(val) {
	return val * 2;
	});
}
```

## ES2015 Arrow Functions Shorthand

Refactor the above code to use two arrow functions. Turn it into a one-liner.

```js
/* Write an ES2015 Version */
const double = arr => arr.map(val => val * 2);
```

## Refactor the following function to use arrow functions:

Replace ALL functions with arrow functions:

```js
function squareAndFindEvens(numbers){
	var squares = numbers.map(function(num){
	return num ** 2;
	});
	var evens = squares.filter(function(square){
	return square % 2 === 0;
	});
	return evens;
}
```
	
Solution:
	
```js
const squareAndFindEvens = numbers => numbers.map(num => num ** 2).filter(square => square % 2 === 0);
```

## Solution

See [Our solution](http://curric.rithmschool.com/springboard/exercises/js-arrow-functions/solution/index.html).
