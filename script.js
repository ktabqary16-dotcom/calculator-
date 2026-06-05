let display = document.getElementById('display');
let currentNumber = '0';
let lastNumber = '';
let currentOperator = '';
let startNewNumber = true;

function updateDisplay() {
    display.textContent = currentNumber;
}

function appendNumber(num) {
    if (startNewNumber) {
        currentNumber = num;
        startNewNumber = false;
    } else {
        currentNumber += num;
    }
    updateDisplay();
}

function appendOperator(op) {
    if (!startNewNumber) {
        if (lastNumber && currentOperator) {
            calculate();
        }
        lastNumber = currentNumber;
        currentOperator = op;
        startNewNumber = true;
    }
}

function calculate() {
    if (!lastNumber || !currentOperator) return;
    
    let result = 0;
    let num1 = parseFloat(lastNumber);
    let num2 = parseFloat(currentNumber);
    
    switch(currentOperator) {
        case '+': result = num1 + num2; break;
        case '-': result = num1 - num2; break;
        case '*': result = num1 * num2; break;
        case '/': result = num2 !== 0 ? num1 / num2 : 0; break;
    }
    
    currentNumber = result.toString();
    if (currentNumber.endsWith('.0')) {
        currentNumber = currentNumber.slice(0, -2);
    }
    lastNumber = '';
    currentOperator = '';
    startNewNumber = true;
    updateDisplay();
}

function clearDisplay() {
    currentNumber = '0';
    lastNumber = '';
    currentOperator = '';
    startNewNumber = true;
    updateDisplay();
}

function backspace() {
    if (currentNumber.length > 1) {
        currentNumber = currentNumber.slice(0, -1);
    } else {
        currentNumber = '0';
        startNewNumber = true;
    }
    updateDisplay();
}

updateDisplay();
