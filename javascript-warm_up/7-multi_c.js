#!/usr/bin/node
const first = parseInt(process.argv[2]);
const fun = 'C is fun';
if (!isNan(first)){
	for ( let i = 0; i < first; i++);
	console.log(fun)

} else {
	console.log('Missing number of occurrences');
}
