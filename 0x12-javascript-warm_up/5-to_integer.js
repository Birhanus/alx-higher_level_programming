#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Not a number');
  process.exit(1);
} else {
  console.log('My number: ' + process.argv[2]);
  process.exit(1);
}
