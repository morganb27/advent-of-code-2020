const fs = require('fs');

function read_file(file_path) {
    const content = fs.readFileSync(file_path, 'utf-8');
    const lines = content.split("\n");
    return lines.map(Number);
}

const file_path = 'input.txt';
const data = read_file(file_path);


function twoNumberSum() {
    for (i=0; i<data.length;i++) {
        for (j=i+1; j<data.length; j++) {
            if (data[i] + data[j] === 2020) {
                return data[i] * data[j]
            }
        }
    }
}

function threeNumberSum() {
    for (i=0; i<data.length;i++) {
        for (j=i+1; j<data.length; j++) {
            for (k=j+1; k<data.length;k++) {
                if (data[i] + data[j] + data[k] === 2020) {
                    return data[i] * data[j] * data[k]
                }
            }
        }
    }
}

console.log(twoNumberSum());
console.log(threeNumberSum());