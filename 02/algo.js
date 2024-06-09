const fs = require('fs');

function read_file(file_path) {
    const content = fs.readFileSync(file_path, 'utf-8');
    const lines = content.split("\n");
    return lines.map(String);
}

const file_path = 'input.txt';
const data = read_file(file_path);

function CalculateNumberOfValidPassword() {
    let organizedData = OrganizingData();
    let primaryCounter = 0;
    for (let i =0; i<organizedData.length;i++) { 
        let [minimumNumberOfOccurences, maximumNumberOfOccurences] = organizedData[i][0].split("-");
        let letterToCheck = organizedData[i][1][0];
        let password = organizedData[i][2];
        let secondaryCounter = 0;
        for (let j=0; j < password.length; j++) {
            if (letterToCheck === password[j]){
                secondaryCounter++
            }
        }
        if (minimumNumberOfOccurences <= secondaryCounter && secondaryCounter <= maximumNumberOfOccurences)
        primaryCounter++
    }
    return primaryCounter;
    
}

function CalculateNumberOfValidPasswordBis() {
    let organizedData = OrganizingData();
    let counter = 0;
    for (let i =0; i<organizedData.length;i++) { 
        let [letterPosition1, letterPosition2] = organizedData[i][0].split("-");
        let letterToCheck = organizedData[i][1][0];
        let password = organizedData[i][2];
        if((letterToCheck === password[parseInt(letterPosition1)-1]) !== (letterToCheck === password[parseInt(letterPosition2)-1])) {
            counter++
        }
    }
    return counter; 
}



function OrganizingData() {
    let organizedData = data.map(item => {
        return item.split(" ");
    })
    return organizedData;
}

console.log(CalculateNumberOfValidPassword());
console.log(CalculateNumberOfValidPasswordBis())