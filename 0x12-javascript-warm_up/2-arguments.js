#!/usr/bin/node
// import { argv } from 'process';

if (process.argv.length === 2) {
  console.log('No argument');
  process.exit(1);
}
if (process.argv.length === 3) {
  console.log('Argument found');
  process.exit(1);
}
if (process.argv.length > 3) {
  console.log('Arguments found');
  process.exit(1);
}
